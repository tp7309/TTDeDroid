# TTDeDroid
[![Build Status](https://travis-ci.org/tp7309/TTDeDroid.svg?branch=master)](https://travis-ci.org/tp7309/TTDeDroid)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2778d8960e094469bc7d4b04d28eb059)](https://www.codacy.com/app/tp7309/TTDeDroid?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tp7309/TTDeDroid&amp;utm_campaign=Badge_Grade)
<!-- [![Coverage Status](https://coveralls.io/repos/github/tp7309/TTDeDroid/badge.svg?branch=master)](https://coveralls.io/github/tp7309/TTDeDroid?branch=master) -->

一键反编译，没什么技术含量，只是调调工具命令，脚本找个放的地方，会视情况更新工具版本。

> - dex2jar=2.1 by DexPatcher
> - jdgui=1.4.0
> - apktool=2.3.0

# 使用要求
需要Python环境，没有的[下载](https://www.python.org/downloads/)一个默认安装完成即可。

## 使用
### Windows
把要查看源码的`*.apk/*.aar/*.dex/*.jar`之类文件复制到当前目录，拖拽文件到`drag_here_if_windows.bat`，一会儿便会自动打开jd-gui。
### Mac or Linux
```
python showjar.py test.apk
```

需要反编译资源的到*showjar.py*中将`_NEED_DECOMPILE_RESOURCES`值置为1即可。

## TODO
抽时间增加更多反编译工具。