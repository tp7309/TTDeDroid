#!/usr/bin python3
import shutil
import os
import stat
import subprocess
import webbrowser


_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def readonly_handler(func, path, execinfo):
    # or os.chmod(path, stat.S_IWRITE) from "stat" module
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmtree(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path, onerror=readonly_handler)
        else:
            os.remove(path)


def repack():
    download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    zippath = os.path.join(download_dir, "TTDeDroid.7z")
    destdir = os.path.abspath(os.path.join(download_dir, 'TTDeDroid'))

    print("start copy dir:")
    rmtree(zippath)
    rmtree(destdir)
    shutil.copytree(_ROOT_PATH, destdir)
    # subprocess.call("cp -r %s %s"%(_ROOT_PATH, destdir), shell=True)
    os.chdir(destdir)
    rmtree(".git")
    rmtree("sources")
    rmtree("cache")
    rmtree("dist")
    rmtree("build")
    rmtree(".vscode")
    rmtree(".history")
    rmtree("__pycache__")
    rmtree('.DS_Store')
    print("7z a %s %s"%(zippath, os.path.join(destdir, '*')))
    subprocess.call("7z a %s %s"%(zippath, os.path.join(destdir, '*')))
    if os.path.exists(zippath):
        print("zip file pack done")


def build_executable_file():
    os.chdir(_ROOT_PATH)
    subprocess.call("pyinstaller -F showjar.py", shell=True)
    if os.path.exists("bin/showjar.bat"):
        os.rename("bin/showjar.bat", "bin/bak_showjar.bat")
    if os.path.exists("bin/bak_showjar.exe"):
        os.remove("bin/bak_showjar.exe")
    shutil.copyfile("dist/showjar.exe", "bin/showjar.exe")


def upload_to_mirror():
    webbrowser.open_new_tab('https://gitee.com/tp7309/ReleaseRepo/tree/master/TTDeDroid')


if __name__ == '__main__':
    build_executable_file()
    repack()
    upload_to_mirror()
