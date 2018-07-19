#!/usr/bin python3
# 自动更新Libs

import subprocess
import shutil
import time
import stat
import os
import glob
import zipfile
import showjar


_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
_SOURCE_DIR = os.path.join(_ROOT_PATH, 'sources')


def sh(command, print_msg=True):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    if print_msg:
        print(result)
    return result


def run(command):
    print(command + '...')
    subprocess.call(command, shell=True)


def ensure_dir(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def readonly_handler(func, path, execinfo):
    # or os.chmod(path, stat.S_IWRITE) from "stat" module
    os.chmod(path, stat.S_IWRITE)
    func(path)


def ensure_repo(origin_url, dirname):
    if os.path.exists(dirname):
        os.chdir(os.path.join(_SOURCE_DIR, dirname))
        print("changed dir to %s"%(os.getcwd()))
        run('git reset --hard HEAD')
        run('git pull --rebase')
    else:
        shutil.rmtree(dirname, onerror=readonly_handler)
        run("git clone %s"%(origin_url))
        os.chdir(os.path.join(_SOURCE_DIR, dirname))
        print("changed dir to %s"%(os.getcwd()))


def dex2jar_update():
    rawdir = os.getcwd()
    os.chdir(_SOURCE_DIR)
    ensure_repo('https://github.com/pxb1988/dex2jar.git', 'dex2jar')
    run("git checkout %s"%(sh('git describe --abbrev=0')))
    run('gradle clean distZip')

    distzipdir = os.path.join('dex2jar', 'dex-tools', 'build', 'distributions')
    distzips = glob.glob("%s/dex-tools*.zip"%(distzipdir))
    if distzips:
        shutil.rmtree(showjar.DEX2JAR, onerror=readonly_handler)
        with zipfile.ZipFile(distzips[0], 'r') as z:
            z.extractall(showjar.DEX2JAR)
        src = os.listdir(showjar.DEX2JAR)[0]
        shutil.move(src, showjar.DEX2JAR)
        shutil.rmtree(src, onerror=readonly_handler)

    os.chdir(rawdir)


def main():
    ensure_dir(_SOURCE_DIR)
    dex2jar_update()


if __name__ == '__main__':
    main()
