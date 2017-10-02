# Android一键反编译辅助脚本
一键反编译，没什么技术含量，只是调调工具命令，脚本找个放的地方，会视情况更新工具版本。

dex2jar="dex2jar-2.1-SNAPSHOT\d2j-dex2jar.bat"
jdgui="jd-gui-1.4.0.jar"
apktool="apktool_2.2.4.jar"

# 使用要求
需要Python环境，没有的[下载](https://www.python.org/downloads/)一个默认安装完成即可。

## 使用
### Windows
把要查看源码的`·*.apk/*.aar/*.dex/*.jar`之类文件复制到当前目录，拖拽文件到`drag_here_if_windows.bat`，一会儿便会自动打开jd-gui。
### Mac or Linux
python showjar.py test.apk

需要反编译资源的到`showjar.py`中将`needDecompileResources`值置为1即可。