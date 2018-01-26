# AndroidOneKeyDecompiler
[![Build Status](https://travis-ci.org/tp7309/AndroidOneKeyDecompiler.svg?branch=master)](https://travis-ci.org/tp7309/AndroidOneKeyDecompiler)
[![Coverage Status](https://coveralls.io/repos/github/tp7309/AndroidOneKeyDecompiler/badge.svg?branch=master)](https://coveralls.io/github/tp7309/AndroidOneKeyDecompiler?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fd2812cdce5d41cd9f829fbdbe429572)](https://www.codacy.com/app/tp7309/AndroidOneKeyDecompiler?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tp7309/AndroidOneKeyDecompiler&amp;utm_campaign=Badge_Grade)

A tool to help quickly decompile apk, update the tools version as appropriate.

> - dex2jar="dex2jar-2.1-SNAPSHOT\d2j-dex2jar.bat"
> - jdgui="jd-gui-1.4.0.jar"
> - apktool="apktool_2.3.0.jar"

README i18n: [中文说明](https://github.com/tp7309/AndroidOneKeyDecompiler/blob/master/README_zh_CN.md)

# Requirements
Python 2 (version 2.7 or later), or Python 3 (version 3.3 or later).

## Usage
### Windows
drag `*.apk/*.aar/*.dex/*.jar` to `drag_here_if_windows.bat`,
`jd-gui` will be automatically opened.
### Mac or Linux
```
python showjar.py *.apk/*.aar/*.dex/*.jar
```
if you need decompile resources, just set `_NEED_DECOMPILE_RESOURCES=1` in *showjar.py*.