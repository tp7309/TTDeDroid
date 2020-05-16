# TTDeDroid
[![Build Status](https://travis-ci.org/tp7309/TTDeDroid.svg?branch=master)](https://travis-ci.org/tp7309/TTDeDroid)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2778d8960e094469bc7d4b04d28eb059)](https://www.codacy.com/app/tp7309/TTDeDroid?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tp7309/TTDeDroid&amp;utm_campaign=Badge_Grade)
<!-- [![Coverage Status](https://coveralls.io/repos/github/tp7309/TTDeDroid/badge.svg?branch=master)](https://coveralls.io/github/tp7309/TTDeDroid?branch=master) -->

一键反编译 **apk/aar/dex/jar**，没什么技术含量，只是调调工具命令，处理些兼容性问题，会视反编译库的更新情况更新工具版本。

> - update at 2020-04-10
>
> - jadx=1.1.0
> - Storyyeller/enjarify(build by source)
> - dex2jar(build by source)
> - jdgui=1.6.6
> - apktool=2.4.1
> - cfr=0.149

# 使用要求
只是使用的话**不需要**手动安装python环境。

## 快速开始

### Windows
1. [去release页下载](https://github.com/tp7309/TTDeDroid/releases)，有中国下载地址能下载快些，也可以直接下载源码。
2. 将`TTDedroid\bin`目录的 **绝对路径** 加入`PATH`环境变量。

之后便可以在任何目录执行下面的目录反编译`*.apk/*.aar/*.dex/*.jar`文件，反编译完成后图形界面会自动打开。
```
showjar test.apk
```

### Mac/Linux
[去release页下载](https://github.com/tp7309/TTDeDroid/releases)，有中国下载地址能下载快些。
```bash
//也可以直接下载源码，中国下载慢，不推荐。
//git clone --depth=1 https://github.com/tp7309/TTDeDroid.git ~/Documents/TTDeDroid

//给脚本执行权限
chmod a+x ~/Documents/TTDeDroid/bin/showjar

//添加脚本执行路径到环境变量
showjardir='export PATH=$PATH:'$HOME/Documents/TTDeDroid/bin
# Mac
echo $showjardir >> ~/.bash_profile && source ~/.bash_profile
# Linux
echo $showjardir >> ~/.bashrc && source ~/.bashrc
```

之后便可以在任何目录执行下面的命令反编译`*.apk/*.aar/*.dex/*.jar`文件，反编译完成后图形界面会自动打开。
```bash
showjar test.apk
```

## 使用

```
usage: showjar.py [-h] [-o [OUTPUT]] [-r [RES]] [-e [ENGINE]] file

Android一键反编译工具

必选参数:
  file                  输入文件路径, *.apk/*.aar/*.dex/*.jar

可选参数:
  -h, --help            显示帮助信息
  -o [OUTPUT], --output [OUTPUT]
                        反编译文件输出目录，可选 (默认: None)
  -r [RES], --res [RES]
                        指定是否要反编译资源文件, 0:禁用, 1:启用 (默认: 0)
  -e [ENGINE], --engine [ENGINE]
                        反编译引擎, [jadx, dex2jar, enjarify, cfr] (默认:
                        jadx)
```
