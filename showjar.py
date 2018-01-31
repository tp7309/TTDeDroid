#!/usr/bin/env python
# -*- coding:utf-8 -*-

# author: tp7309
# usage:
# python showjar.py *.apk/*.aar/*.dex/*.jar

from __future__ import print_function

import os
import shutil
import subprocess
import sys
import zipfile

_LIBS = os.path.abspath('libs')
_DEX2JAR = os.path.join(_LIBS, 'dex2jar-2.1-20171001-lanchon',
                        'd2j-dex2jar.bat')
if not os.name == 'nt':
    _DEX2JAR = 'sh ' + os.path.join(_LIBS, 'dex2jar-2.1-20171001-lanchon',
                                    'd2j-dex2jar.sh')
_JDGUI = os.path.join(_LIBS, 'jd-gui-1.4.0.jar')
_APKTOOL = os.path.join(_LIBS, 'apktool_2.3.0.jar')

_CACHE_DIR = 'cache'
_NEED_UNZIP_FILES = ['patch.jar']
_TEST_MODE = False
_NEED_DECOMPILE_RESOURCES = 0


def sh(command):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p.stdout.read())


def main(f):
    # fix windows path
    if ":\\" in f and ":\\\\" not in f:
        f = f.replace("\\", "\\\\")

    # build cache dir
    shutil.rmtree(_CACHE_DIR, ignore_errors=True)
    if not os.path.exists(_CACHE_DIR):
        os.mkdir(_CACHE_DIR)

    dexes = []
    jars = []
    temp_dir = os.path.abspath(
        os.path.join(_CACHE_DIR,
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

    if _NEED_DECOMPILE_RESOURCES and f.endswith(
            ".apk") or f in _NEED_UNZIP_FILES:
        print("decompile resources...")
        sh("java -jar %s d %s -o %s" % (_APKTOOL, f, _CACHE_DIR))
        print("decompile resources done")

    if jars and not _TEST_MODE:
        sh("java -jar %s %s" % (_JDGUI, ' '.join(jars)))
    print("Done")


if __name__ == "__main__":
    main(sys.argv[1])
