# TTDeDroid
[![Build Status](https://github.com/tp7309/TTDeDroid/actions/workflows/build.yaml/badge.svg?branch=master)](https://github.com/tp7309/TTDeDroid/actions/workflows/build.yaml)
[![DeepSource](https://deepsource.io/gh/tp7309/TTDeDroid.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/tp7309/TTDeDroid/?ref=repository-badge)
<!-- [![codecov](https://codecov.io/gh/tp7309/TTDeDroid/branch/master/graph/badge.svg?token=lyEWTqfeb9)](https://codecov.io/gh/tp7309/TTDeDroid) -->
README i18n: [中文说明](https://github.com/tp7309/TTDeDroid/blob/master/README_zh_CN.md)

The tool for quickly decompile **apk/aar/dex/jar**, will be updated depending on the update of libs.

> - update at 2022-10-22
>
> - jadx=1.4.5
> - Storyyeller/enjarify(build by source)
> - dex2jar(build by source)
> - fernflower=222.4345.14(IntelliJ IDEA official decompiler)
> - apktool=2.6.1

# Requirements
No need to install python environment.

## Quick Start
### Windows
1. go to `releases` page to download file or download source code.
2. add `TTDedroid\bin` directory **absolute path** to `PATH` system variable.
3. then you can execute command for decompile `*.apk/*.aar/*.dex/*.jar` anywhere, GUI will be automatically opened.
```bash
showjar test.apk
```
### Mac/Linux
run following commands:
```bash
git clone --depth=1 https://github.com/tp7309/TTDeDroid.git ~/Documents/TTDeDroid
chmod a+x ~/Documents/TTDeDroid/bin/showjar
showjardir='export PATH=$PATH:'$HOME/Documents/TTDeDroid/bin
# Mac
echo $showjardir >> ~/.bash_profile && source ~/.bash_profile
# Linux
echo $showjardir >> ~/.bashrc && source ~/.bashrc
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
                        decompiler engine, [jadx, dex2jar, fernflower, enjarify] (default:
                        jadx)
```
