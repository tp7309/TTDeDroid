# TTDeDroid
[![Build Status](https://travis-ci.org/tp7309/TTDeDroid.svg?branch=master)](https://travis-ci.org/tp7309/TTDeDroid)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2778d8960e094469bc7d4b04d28eb059)](https://www.codacy.com/app/tp7309/TTDeDroid?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tp7309/TTDeDroid&amp;utm_campaign=Badge_Grade)
<!-- [![Coverage Status](https://coveralls.io/repos/github/tp7309/TTDeDroid/badge.svg?branch=master)](https://coveralls.io/github/tp7309/TTDeDroid?branch=master) -->

一键反编译，没什么技术含量，只是调调工具命令，脚本找个放的地方，会视情况更新工具版本。

> - update at 2018-07-24

> - jadx=0.8.0
> - Storyyeller/enjarify
> - dex2jar=2.1
> - jdgui=1.4.0
> - apktool=2.3.4
> - cfr

# 使用要求
需要Python环境，没有的[下载](https://www.python.org/downloads/)一个默认安装完成即可。

## 快速开始
### Windows
1. 将`bin`目录的 **绝对路径** 加入`PATH`系统变量。
2. 之后便可以在任何目录执行下面的目录反编译`*.apk/*.aar/*.dex/*.jar`文件，反编译完成后图形界面会自动打开。
```
showjar test.apk
```
### Mac or Linux
```
python showjar.py test.apk
```

## 使用
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
                        decompilation engine, [jadx, dex2jar, enjarify, cfr] (default:
                        jadx)
```
