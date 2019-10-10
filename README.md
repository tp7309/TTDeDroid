# TTDeDroid
[![Build Status](https://travis-ci.org/tp7309/TTDeDroid.svg?branch=master)](https://travis-ci.org/tp7309/TTDeDroid)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2778d8960e094469bc7d4b04d28eb059)](https://www.codacy.com/app/tp7309/TTDeDroid?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tp7309/TTDeDroid&amp;utm_campaign=Badge_Grade)
<!-- [![Coverage Status](https://coveralls.io/repos/github/tp7309/TTDeDroid/badge.svg?branch=master)](https://coveralls.io/github/tp7309/TTDeDroid?branch=master) -->
README i18n: [中文说明](https://github.com/tp7309/AndroidOneKeyDecompiler/blob/master/README_zh_CN.md)

The tool for quickly decompile **apk/aar/dex/jar**, will be updated depending on the update of libs.

> - update at 2019-04-17
>
> - jadx=0.9.0
> - Storyyeller/enjarify(build by source)
> - dex2jar(build by source)
> - jdgui=1.4.2
> - apktool=2.4.0
> - cfr=0.143

# Requirements
Python 2 (version 2.7 or later), or Python 3 (version 3.5 or later).

## Quick Start
### Windows
1. add `TTDedroid\bin` directory **absolute path** to `PATH` system variable.
2. then you can execute command for decompile `*.apk/*.aar/*.dex/*.jar` anywhere, GUI will be automatically opened.
```bash
showjar test.apk
```
### Mac/Linux
run following commands:
```bash
git clone --depth=1 https://github.com/tp7309/TTDeDroid.git ~/Documents/TTDeroid
chmod a+x ~/Documents/TTDeroid/bin/showjar
echo 'export PATH=$PATH:~/Documents/TTDedroid/bin' >> ~/.bash_profile && source ~/.bash_profile
```
then you can execute command for decompile `*.apk/*.aar/*.dex/*.jar` anywhere, GUI will be automatically opened.
```bash
showjar test.apk
```

## Usage
```
usage: showjar.py [-h] [-o [OUTPUT]] [-r [RES]] [-e [ENGINE]] file

android decompile tool

positional arguments:
  file                  input file path, *.apk/*.aar/*.dex/*.jar

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
                        output directory, optional (default: None)
  -r [RES], --res [RES]
                        decode resources, 0:disable, 1:enable (default: 0)
  -e [ENGINE], --engine [ENGINE]
                        decompiler engine, [jadx, dex2jar, enjarify, cfr] (default:
                        jadx)
```
