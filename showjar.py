#!/usr/bin/env python
# -*- coding:utf-8 -*-

#author: tp7309
#usage:
#python showjar.py *.apk/*.aar/*.dex/*.jar


from __future__ import print_function

import os
import shutil
import subprocess
import sys
import zipfile

dex2jar="dex2jar-2.1-SNAPSHOT\d2j-dex2jar.bat"
if not os.name == 'nt': dex2jar = "./dex2jar-2.1-SNAPSHOT/d2j-dex2jar.sh"
jdgui="jd-gui-1.4.0.jar"
apktool="apktool_2.3.0.jar"
needUnzipFiles=['patch.jar']
needDecompileResources=0

#unpack
#java -jar apktool_2.2.4.jar d test.apk
#repack
#java -jar apktool_2.2.4.jar b test


def sh(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p.stdout.read())


if __name__=="__main__":
    f = sys.argv[1]
    # fix windows path
    if ":\\" in f and not ":\\\\" in f:
            f = f.replace("\\", "\\\\")
    dexes = []
    jars = []
    if f.endswith(".apk") or f in needUnzipFiles:
        print("unzip %s..."%(f))
        tempDir = os.path.splitext(f)[0]
        with zipfile.ZipFile(f, 'r') as zip:
            zip.extractall(tempDir)
        dexes = [f for f in os.listdir(tempDir) if f.endswith('.dex')]
        print("founded dexes: " + ', '.join(dexes))
        for file in os.listdir(tempDir):
            if file.endswith('-dex2jar.jar') and os.path.exists(file):
                os.remove(file)
        for dex in dexes:
            sh("%s -f %s"%(dex2jar, os.path.join(tempDir, dex)))
            jars.append(os.path.splitext(dex)[0] + "-dex2jar.jar")
        shutil.rmtree(tempDir)
    elif f.endswith(".aar"):
        print("unzip %s..."%(f))
        tempDir = os.path.splitext(f)[0]
        with zipfile.ZipFile(f, 'r') as zip:
        	zip.extractall(tempDir)
        dstPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "classes.jar")
        shutil.move(os.path.join(tempDir, "classes.jar"), dstPath)
        shutil.rmtree(tempDir)
        jars.append("classes.jar")	
    elif f.endswith(".dex"):
        sh("%s -f %s"%(dex2jar, f))
        jars.append(os.path.splitext(f)[0] + "-dex2jar.jar")
    elif f.endswith(".jar"):
        jars.append(f)
    else:
        print("error file extension!")
        exit

    if needDecompileResources and f.endswith(".apk") or f in needUnzipFiles:
        print("decompile resources...")
        sh("java -jar %s d %s"%(apktool, f))
        print("decompile resources done")
            
    sh("java -jar %s %s"%(jdgui, ' '.join(jars) if len(jars)> 0 else jars[0]))
    print("Done")
