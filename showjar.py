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
import stat
import fnmatch
import re

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    bundle_dir = os.path.abspath(os.path.join(os.path.dirname(sys.executable), os.path.pardir))
else:
    # we are running in a normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
_ROOT_PATH = bundle_dir
print("root path: " + _ROOT_PATH)

_LIBS = os.path.join(_ROOT_PATH, 'libs')

DEX2JAR = os.path.join(_LIBS, 'dex2jar')
JDGUI = os.path.join(_LIBS, 'jd-gui')
APKTOOL = os.path.join(_LIBS, 'apktool')
JADX = os.path.join(_LIBS, 'jadx')
ENJARIFY = os.path.join(_LIBS, 'enjarify')
CFR = os.path.join(_LIBS, 'cfr')

CACHE_DIR = os.path.join(_ROOT_PATH, 'cache')
# may be robust patch file, match full path.
_NEED_UNZIP_FILES = ['patch.jar']


def newshell(command):
    if os.name == 'nt':
        return "start cmd /c %s" % (command)
    else:
        return "sh -c %s" % (command)


def sh(command, print_msg=True):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    if print_msg:
        print(result)
    return result


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


# clean strange file name
def clean_filename(cache, path):
    name = os.path.basename(path)
    pattern = re.compile(u"[-\.\(\)\w]+")
    name2 = '_'.join(re.findall(pattern, name))
    if name != name2:
        newname = "ttdedroid_%s"%(name2)
        newpath = os.path.join(cache, newname)
        shutil.copyfile(path, newpath)
        return newpath
    return path


def main():
    parser = argparse.ArgumentParser(description='android decompile tool',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o', '--output', nargs='?',
                        help='output directory, optional')
    parser.add_argument('-r', '--res', nargs='?', type=int, default=0,
                        help='decode resources, 0:disable, 1:enable')
    parser.add_argument('-e', '--engine', nargs='?', default='jadx',
                        help='decompiler engine, [jadx, dex2jar, enjarify, cfr]')
    parser.add_argument('-t', nargs='?', type=int,
                        default=0, help=argparse.SUPPRESS)
    parser.add_argument(
        'file', help='input file path, *.apk/*.aar/*.dex/*.jar')
    args = parser.parse_args()

    if args.output:
        args.output = os.path.join(os.getcwd(), args.output)
    cache = args.output if args.output else CACHE_DIR

    # recreate cache dir
    if os.path.abspath(cache) == os.path.abspath(CACHE_DIR):
        print("clearing cache...")
        rmtree(CACHE_DIR)
        print("clear cache done")
    if not os.path.exists(cache):
        os.mkdir(cache)

    f = os.path.join(os.getcwd(), args.file)
    f = clean_filename(cache, f)
    # fix windows path
    if ":\\" in f and ":\\\\" not in f:
        f = f.replace("\\", "\\\\")
    args.file = f

    print("output dir: %s" % (cache))
    if args.engine == 'jadx':
        decompile_by_jadx(cache, args)
    elif args.engine == 'enjarify':
        decompile_by_enjarify(cache, args)
    elif args.engine == 'cfr':
        decompile_by_cfr(cache, args)
    else:
        decompile_by_dex2jar(cache, args)
    clean_temp_error_files()
    print("\nDone")


def readonly_handler(func, path, execinfo):
    # or os.chmod(path, stat.S_IWRITE) from "stat" module
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmtree(path):
    if os.path.exists(path):
        shutil.rmtree(path, onerror=readonly_handler)


def hasexec(cmd):
    result = sh("%s --version" % (cmd), print_msg=False)
    return not ('not found' in result or u'不是' in result)


def openfile(path):
    # open with vscode by default
    if hasexec('code'):
        run("code \"%s\""%(path))
        return

    if os.name == 'nt':
        run("start %s" % (path))
    else:
        run("open %s" % (path))


def find_files(directory, pattern):
    filenames = []
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                filenames.append(filename)
    return filenames


def findjar(dirpath, rejar):
    jars = glob.glob("%s/%s" % (dirpath, rejar))
    if jars:
        return jars[0]
    return ''


def jdguipath():
    return findjar(JDGUI, 'jd-gui*.jar')


def apktoolpath():
    return findjar(APKTOOL, 'apktool*.jar')


def jadxpath():
    if os.name == 'nt':
        return os.path.join(JADX, 'bin', 'jadx-gui.bat')
    else:
        return os.path.join(JADX, 'bin', 'jadx-gui')


def cfrpath():
    return findjar(CFR, 'cfr*.jar')


def decompile_by_cfr(cache, args):
    print('use dex2jar to extract jars...')
    jars = dex2jar(cache, args)
    if not jars:
        print("unsupport decompile %s" % (args.file))
        return
    name = os.path.splitext(os.path.basename(args.file))[0]
    cache_path = os.path.join(cache, name)

    for jar in jars:
        run("java -Xms256m -Xmx1024m -jar %s %s --outputdir %s" %
            (cfrpath(), jar, cache_path))
    if args.t == 0:
        openfile(cache_path)


def decompile_by_enjarify(cache, args):
    if not args.file.endswith('.apk') and not args.file.endswith('.dex'):
        print("enjarify only support apk/dex file!")
        return

    if sys.version_info < (3, 5):
        print("enjarify only support python3")
        return

    deres(cache, args)
    os.chdir(ENJARIFY)
    enjarify = 'enjarify.bat' if os.name == 'nt' else './enjarify.sh'
    make_executable(enjarify)
    output_file = os.path.join(cache, "%s-enjarify.jar" %
                               (os.path.splitext(os.path.basename(args.file))[0]))
    run("%s -o %s %s" % (enjarify, output_file, args.file))
    jars = glob.glob("%s/*.jar" % (cache))
    if jars and args.t == 0:
        run("java -jar %s %s" % (jdguipath(), ' '.join(jars)))


def decompile_by_jadx(cache, args):
    # support *.apk/*.aar/*.dex/*.jar
    inputs = [args.file]
    make_executable(jadxpath())
    for file in inputs:
        if args.res == 1:
            run("%s -r -j 8 %s" % (jadxpath(), file))
        else:
            run("%s -j 8 %s" % (jadxpath(), file))


def dex2jar(cache, args):
    cmd = os.path.join(DEX2JAR, 'd2j-dex2jar.bat')
    if not os.name == 'nt':
        cmd = os.path.join(DEX2JAR, 'd2j-dex2jar.sh')
        run("chmod a+x %s" % (cmd))
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
            run("%s -f %s -o %s" % (cmd, dex, dest))
            if not os.path.exists(dest):
                print("\n%s decompile failed!\n" % (dest))
            else:
                jars.append(dest)
    elif args.file.endswith(".aar"):
        print("unzip %s..." % (args.file))
        with zipfile.ZipFile(args.file, 'r') as z:
            z.extractall(temp_dir)
        # maybe has ''libs' directory
        jars.extend(find_files(temp_dir, "*.jar"))
    elif args.file.endswith(".dex"):
        dest = os.path.join(temp_dir, "classes-dex2jar.jar")
        print(dest)
        run("%s -f %s -o %s" % (cmd, args.file, dest))
        if not os.path.exists(dest):
            print("%s decompile failed!" % (dest))
        else:
            jars.append(dest)
    elif args.file.endswith(".jar"):
        jars.append(args.file)
    else:
        print("error file extension!")

    resdest = os.path.join(cache, 'res')
    print("when decompile resources done, resources stored in: %s" % (resdest))
    return jars


def decompile_by_dex2jar(cache, args):
    jars = dex2jar(cache, args)
    if jars and not args.t == 1:
        run("java -jar %s %s" % (jdguipath(), ' '.join(jars)))


def deres(cache, args):
    if args.res == 1 and args.file.endswith(".apk"):
        print("decompile resources...")
        resdest = os.path.join(cache, 'res')
        run(newshell("java -jar %s d %s -f -o %s" %
                     (apktoolpath(), args.file, resdest)))
        print("decompile resources done, path: %s" % (resdest))


if __name__ == "__main__":
    main()
