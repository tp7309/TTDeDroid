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
FERNFLOWER = os.path.join(_LIBS, 'fernflower')

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
    pattern = re.compile(u"[-\\.\\w]+")
    name2 = '_'.join(re.findall(pattern, name))
    if name != name2:
        newname = "ttdedroid_%s"%(name2)
        newpath = os.path.join(cache, newname)
        shutil.copyfile(path, newpath)
        return newpath
    return path


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


def find_jdk11_or_greater_version():
    def isValidJdk(jdkpath):
        re_jdk_version = r'\"(\d+)\.(\d+)\.(\d+).*\"'
        try:
            # print(jdkpath)
            result = re.findall(re_jdk_version, sh("\"%s\" -version"%(jdkpath), print_msg=False))
            print("find java version: %s"%(result))
            if not result:
                return False
            result = result[0]
            major_version = int(result[0])
            second_version = int(result[1])
            # print("%i.%i"%(major_version, second_version))
            if major_version > 1:
                return True
            else:
                return major_version >= 1 and second_version >= 11
        except Exception as e:
            print(e)
            return False

    # check current java version
    if(isValidJdk('java')):
        return 'java'

    files = []
    # find 'java' in "JAVA_HOME" directory
    java_home = os.environ.get('JAVA_HOME', '')
    if java_home:
        # print(java_home)
        java_home_parent_dir = os.path.abspath(os.path.join(java_home, os.path.pardir))
        print("find 'java' in java_home_parent_dir: %s"%(java_home_parent_dir))
        files = files + glob.glob("%s/*/bin/java"%(java_home_parent_dir))
        files = files + glob.glob("%s/*/bin/java.exe"%(java_home_parent_dir))
    jdks_path = os.path.join(os.path.expanduser('~'), '.jdks')
    if jdks_path:
        print("find 'java' in %s"%(jdks_path))
        files = files + glob.glob("%s/*/bin/java"%(jdks_path))
        files = files + glob.glob("%s/*/bin/java.exe"%(jdks_path))
    print("founded jdk locations:")
    print(files)
    for file in files:
        if isValidJdk(file):
            print("found jdk location(jdk>=11): %s"%(file))
            return file
    return None


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


def fernflowerpath():
    return os.path.join(FERNFLOWER, 'fernflower.jar')


def show_jar_gui(files):
    if not files:
        print("not jar input")
    make_executable(jadxpath())
    for jar in files:
        run("java -jar %s %s"%(jdguipath(), jar))
    # filepath = ' '.join(files)
    # print("use jadx to view class reference...")
    # run("%s -j 8 %s" % (jadxpath(), filepath))


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
        show_jar_gui(jars)


def decompile_by_jadx(cache, args):
    # support *.apk/*.aar/*.dex/*.jar
    make_executable(jadxpath())
    if args.res == 1:
        run("%s -r -j 8 %s" % (jadxpath(), args.file))
    else:
        run("%s -j 8 %s" % (jadxpath(), args.file))


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
    print(args.file)
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
        print("invalid file extension!")

    resdest = os.path.join(cache, 'res')
    print("when decompile resources done, resources stored in: %s" % (resdest))
    return jars


def decompile_by_dex2jar(cache, args):
    jars = dex2jar(cache, args)
    if jars and args.t == 0:
        show_jar_gui(jars)


def decompile_by_fernflower(cache, args):
    # support *.apk/*.aar/*.dex/*.jar
    make_executable(fernflowerpath())
    jars = dex2jar(cache, args)
    if not jars:
        return
    print('fernflower need jdk>=11, ensure jdk11 or above version is installed...')
    jdkpath = find_jdk11_or_greater_version()
    if not jdkpath:
        print("fernflower need jdk>=11, but not found!")
        return
    for jar in jars:
        run("%s -jar %s %s %s"%(jdkpath, fernflowerpath(), jar, cache))
    jars = glob.glob("%s/%s"%(cache, "*.jar"))
    print(jars)
    if jars and args.t == 0:
        show_jar_gui(jars)


def deres(cache, args):
    if args.res == 1 and args.file.endswith(".apk"):
        print("decompile resources...")
        resdest = os.path.join(cache, 'res')
        run(newshell("java -jar %s d %s -f -o %s" %
                     (apktoolpath(), args.file, resdest)))
        print("decompile resources done, path: %s" % (resdest))


def main():
    parser = argparse.ArgumentParser(description='android decompile tool',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o', '--output', nargs='?',
                        help='output directory, optional')
    parser.add_argument('-r', '--res', nargs='?', type=int, default=0,
                        help='decode resources, 0:disable, 1:enable')
    parser.add_argument('-e', '--engine', nargs='?', default='jadx',
                        help='decompiler engine, [jadx, dex2jar, enjarify,fernflower]')
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

    f = args.file
    if not os.path.isabs(args.file):
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
    elif args.engine == 'fernflower':
        decompile_by_fernflower(cache, args)
    else:
        decompile_by_dex2jar(cache, args)
    clean_temp_error_files()
    print("\nDone")


if __name__ == "__main__":
    main()
