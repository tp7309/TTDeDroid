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


_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
_LIBS = os.path.join(_ROOT_PATH, 'libs')
_DEX2JAR = os.path.join(_LIBS, 'dex2jar-2.1-20171001-lanchon',
                        'd2j-dex2jar.bat')
if not os.name == 'nt':
    _DEX2JAR = 'sh ' + os.path.join(_LIBS, 'dex2jar-2.1-20171001-lanchon',
                                    'd2j-dex2jar.sh')
_JDGUI = os.path.join(_LIBS, 'jd-gui-1.4.0.jar')
_APKTOOL = os.path.join(_LIBS, 'apktool_2.3.2.jar')

_JADX = os.path.join(_LIBS, 'jadx-0.7.1', 'bin', 'jadx-gui')

_CACHE_DIR = os.path.join(_ROOT_PATH, 'cache')
_NEED_UNZIP_FILES = ['patch.jar']


def sh(command):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p.stdout.read())


def clean_temp_error_files():
    # when dex2jar decompile error, some error file generated.
    files = glob.glob("%s/classes?-error.zip"%(_ROOT_PATH))
    for file in files:
        os.remove(file)


def main():
    parser = argparse.ArgumentParser(description='android decompile tool',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--output', nargs='?', help='output directory, optional')
    parser.add_argument('-r', '--res', nargs='?', type=int, default=0,
                        help='decode resources, 0:disable, 1:enable')
    parser.add_argument('-e', '--engine', nargs='?', default='jadx',
                        help='decompiler engine, [jadx, dex2jar]')
    parser.add_argument('-t', nargs='?', type=int, default=0, help=argparse.SUPPRESS)
    parser.add_argument('file', help='input file path, *.apk/*.aar/*.dex/*.jar')
    args = parser.parse_args()

    f = args.file
    # fix windows path
    if ":\\" in f and ":\\\\" not in f:
        f = f.replace("\\", "\\\\")

    # build cache dir
    print("clearing cache...")
    print(_CACHE_DIR)
    shutil.rmtree(_CACHE_DIR, ignore_errors=True)
    print("clear cache done")
    if not os.path.exists(_CACHE_DIR):
        os.mkdir(_CACHE_DIR)

    if args.engine == 'jadx':
        decompile_by_jadx(f, args)
    else:
        decompile_by_dex2jar(f, args)
    clean_temp_error_files()
    print("\nDone")


def newshell(command):
    if os.name == 'nt':
        return "start cmd /c %s"%(command)
    else:
        return "sh -c %s"%(command)


def run(command):
    subprocess.call(command, shell=True)


def decompile_by_jadx(f, args):
    cache = args.output if args.output else _CACHE_DIR
    temp_dir = os.path.abspath(os.path.join(
        cache, os.path.splitext(os.path.basename(f))[0]))
    # jadx has bug when pass .aar file, temp solution.
    if f.endswith(".aar"):
        print("unzip %s..." % (f))
        with zipfile.ZipFile(f, 'r') as z:
            z.extractall(temp_dir)
        f = os.path.join(temp_dir, "classes.jar")

    # when use jadx-gui, '-d' option not work.
    if args.res == 1:
        sh("%s -r -j 8 %s"%(_JADX, f))
    else:
        sh("%s -j 8 %s"%(_JADX, f))


def decompile_by_dex2jar(f, args):
    dexes = []
    jars = []
    deres(f, args)
    cache = args.output if args.output else _CACHE_DIR
    temp_dir = os.path.abspath(
        os.path.join(cache,
                     os.path.splitext(os.path.basename(f))[0]))
    if f.endswith(".apk") or f in _NEED_UNZIP_FILES:
        print("unzip %s..." % (f))
        with zipfile.ZipFile(f, 'r') as z:
            z.extractall(temp_dir)
        dexes = [
            os.path.join(temp_dir, dex) for dex in os.listdir(temp_dir)
            if dex.endswith('.dex')
        ]
        print("founded dexes: " + ', '.join(dexes))
        for dex in dexes:
            dest = os.path.splitext(dex)[0] + "-dex2jar.jar"
            sh("%s -f %s -o %s" % (_DEX2JAR, dex, dest))
            if not os.path.exists(dest):
                print("\n%s decompile failed!\n"%(dest))
            else:
                jars.append(dest)
    elif f.endswith(".aar"):
        print("unzip %s..." % (f))
        with zipfile.ZipFile(f, 'r') as z:
            z.extractall(temp_dir)
        jars.append(os.path.join(temp_dir, "classes.jar"))
    elif f.endswith(".dex"):
        dest = os.path.join(temp_dir, "classes-dex2jar.jar")
        print(dest)
        sh("%s -f %s -o %s" % (_DEX2JAR, f, dest))
        if not os.path.exists(dest):
            print("%s decompile failed!"%(dest))
        else:
            jars.append(dest)
    elif f.endswith(".jar"):
        jars.append(f)
    else:
        print("error file extension!")
        return

    if jars and not args.t == 1:
        sh("java -jar %s %s" % (_JDGUI, ' '.join(jars)))
    resdest = os.path.join(cache, 'res')
    print("when decompile resources done, store path: %s" % (resdest))


def deres(f, args):
    cache = args.output if args.output else _CACHE_DIR
    if args.res == 1 and f.endswith(
            ".apk") or f in _NEED_UNZIP_FILES:
        print("decompile resources...")
        resdest = os.path.join(cache, 'res')
        run(newshell("cmd /c java -jar %s d %s -f -o %s" % (_APKTOOL, f, resdest)))
        print("decompile resources done, path: %s" % (resdest))


if __name__ == "__main__":
    main()
