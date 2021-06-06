#!/usr/bin python3
import shutil
import os
import stat
import subprocess


_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def readonly_handler(func, path, execinfo):
    # or os.chmod(path, stat.S_IWRITE) from "stat" module
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmtree(path):
    if os.path.exists(path):
        rmtree(path, onerror=readonly_handler)


def main():
    destdir = os.path.join(os.path.expanduser('~'), 'Downloads')
    zippath = os.path.join(destdir, "TTDeDroid.zip")

    rmtree(zippath)
    # shutil.copy(_ROOT_PATH, destdir)
    subprocess.call("cp -r %s %s"%('_ROOT_PATH', destdir), shell=True)
    os.chdir(os.path.join(destdir, "TTDeDroid"))
    rmtree(".git")
    rmtree("sources")
    rmtree("cache")
    rmtree("dist")
    rmtree("build")
    rmtree(".vscode")
    rmtree(".history")
    rmtree("__pycache__")
    os.remove('.DS_Store')
    subprocess.call("7z a %s %s"%(os.path.join(destdir, "TTDeDroid"), zippath))


if __name__ == '__main__':
    main()
