#!/usr/bin/env python
# -*- coding:utf-8 -*-

# author: tp7309
# usage:
# python showjar.py *.apk/*.aar/*.dex/*.jar

from __future__ import print_function

import os
import shutil
import subprocess
import zipfile
import argparse
import glob
import sys


_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
_LIBS = os.path.join(_ROOT_PATH, 'libs')
_DEX2JAR = os.path.join(_LIBS, 'dex2jar-2.1-20171001-lanchon',
                        'd2j-dex2jar.bat')
if not os.name == 'nt':
    _DEX2JAR = os.path.join(_LIBS, 'dex2jar-2.1-20171001-lanchon',
                            'd2j-dex2jar.sh')
_JDGUI = os.path.join(_LIBS, 'jd-gui-1.4.0.jar')
_APKTOOL = os.path.join(_LIBS, 'apktool_2.3.2.jar')

_JADX = os.path.join(_LIBS, 'jadx-0.7.1', 'bin', 'jadx-gui')
_ENJARIFY_DIR = os.path.join(_LIBS, 'enjarify')

_CACHE_DIR = os.path.join(_ROOT_PATH, 'cache')
# may be robust patch file, match full path.
_NEED_UNZIP_FILES = ['patch.jar']


def newshell(command):
    if os.name == 'nt':
        return "start cmd /c %s" % (command)
    else:
        return "sh -c %s" % (command)


def run(command, print_msg=True):
    if print_msg:
        print(command)
    subprocess.call(command, shell=True)


def make_executable(file):
    if not os.name == 'nt':
        run("chmod a+x %s" % (file), print_msg=False)


def clean_temp_error_files():
    # when dex2jar decompile error, some error file generated.
    files = glob.glob("%s/classes?-error.zip" % (_ROOT_PATH))
    for file in files:
        os.remove(file)


def main():
    parser = argparse.ArgumentParser(description='android decompile tool',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o', '--output', nargs='?',
                        help='output directory, optional')
    parser.add_argument('-r', '--res', nargs='?', type=int, default=0,
                        help='decode resources, 0:disable, 1:enable')
    parser.add_argument('-e', '--engine', nargs='?', default='jadx',
                        help='decompiler engine, [jadx, dex2jar, enjarify]')
    parser.add_argument('-t', nargs='?', type=int,
                        default=0, help=argparse.SUPPRESS)
    parser.add_argument(
        'file', help='input file path, *.apk/*.aar/*.dex/*.jar')
    args = parser.parse_args()

    f = os.path.join(os.getcwd(), args.file)
    # fix windows path
    if ":\\" in f and ":\\\\" not in f:
        f = f.replace("\\", "\\\\")
    args.file = f
    if args.output:
        args.output = os.path.join(os.getcwd(), args.output)
    # build cache dir
    print("clearing cache...")
    shutil.rmtree(_CACHE_DIR, ignore_errors=True)
    print("clear cache done")
    if not os.path.exists(_CACHE_DIR):
        os.mkdir(_CACHE_DIR)

    cache = args.output if args.output else _CACHE_DIR
    print("output dir: %s" % (cache))
    if args.engine == 'jadx':
        decompile_by_jadx(cache, args)
    elif args.engine == 'enjarify':
        decompile_by_enjarify(cache, args)
    else:
        decompile_by_dex2jar(cache, args)
    clean_temp_error_files()
    print("\nDone")


def decompile_by_enjarify(cache, args):
    if not args.file.endswith('.apk') and not args.file.endswith('.dex'):
        print("enjarify only support apk/dex file!")
        return

    if sys.version_info < (3, 5):
        print("enjarify only support python3")
        return

    deres(cache, args)
    os.chdir(_ENJARIFY_DIR)
    enjarify = 'enjarify.bat' if os.name == 'nt' else './enjarify.sh'
    make_executable(enjarify)
    output_file = os.path.join(cache, "%s-enjarify.jar" %
                               (os.path.splitext(os.path.basename(args.file))[0]))
    run("%s -o %s %s" % (enjarify, output_file, args.file))
    jars = glob.glob("%s/*.jar" % (cache))
    if jars and not args.t == 1:
        run("java -jar %s %s" % (_JDGUI, ' '.join(jars)))


def decompile_by_jadx(cache, args):
    temp_dir = os.path.abspath(os.path.join(
        cache, os.path.splitext(os.path.basename(args.file))[0]))
    # jadx has bug when pass .aar file, temp solution.
    dest = args.file
    if dest.endswith(".aar"):
        print("unzip %s..." % (args.file))
        with zipfile.ZipFile('r') as z:
            z.extractall(temp_dir)
        dest = os.path.join(temp_dir, "classes.jar")

    make_executable(_JADX)
    # when use jadx-gui, '-d' option not work.
    if args.res == 1:
        run("%s -r -j 8 %s" % (_JADX, dest))
    else:
        run("%s -j 8 %s" % (_JADX, dest))


def decompile_by_dex2jar(cache, args):
    dexes = []
    jars = []
    deres(cache, args)
    temp_dir = os.path.abspath(
        os.path.join(cache,
                     os.path.splitext(os.path.basename(args.file))[0]))
    if args.file.endswith(".apk") or args.file in _NEED_UNZIP_FILES:
        print("unzip %s..." % (args.file))
        with zipfile.ZipFile(args.file, 'r') as z:
            z.extractall(temp_dir)
        dexes = [
            os.path.join(temp_dir, dex) for dex in os.listdir(temp_dir)
            if dex.endswith('.dex')
        ]
        print("founded dexes: " + ', '.join(dexes))
        for dex in dexes:
            dest = os.path.splitext(dex)[0] + "-dex2jar.jar"
            run("%s -f %s -o %s" % (_DEX2JAR, dex, dest))
            if not os.path.exists(dest):
                print("\n%s decompile failed!\n" % (dest))
            else:
                jars.append(dest)
    elif args.file.endswith(".aar"):
        print("unzip %s..." % (args.file))
        with zipfile.ZipFile(args.file, 'r') as z:
            z.extractall(temp_dir)
        jars.append(os.path.join(temp_dir, "classes.jar"))
    elif args.file.endswith(".dex"):
        dest = os.path.join(temp_dir, "classes-dex2jar.jar")
        print(dest)
        run("%s -f %s -o %s" % (_DEX2JAR, args.file, dest))
        if not os.path.exists(dest):
            print("%s decompile failed!" % (dest))
        else:
            jars.append(dest)
    elif args.file.endswith(".jar"):
        jars.append(args.file)
    else:
        print("error file extension!")
        return

    if jars and not args.t == 1:
        run("java -jar %s %s" % (_JDGUI, ' '.join(jars)))
    resdest = os.path.join(cache, 'res')
    print("when decompile resources done, store path: %s" % (resdest))


def deres(cache, args):
    if args.res == 1 and args.file.endswith(".apk"):
        print("decompile resources...")
        resdest = os.path.join(cache, 'res')
        run(newshell("java -jar %s d %s -f -o %s" %
                     (_APKTOOL, args.file, resdest)))
        print("decompile resources done, path: %s" % (resdest))


if __name__ == "__main__":
    main()
