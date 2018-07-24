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


def rmtree(path):
    if os.path.exists(path):
        shutil.rmtree(path, onerror=readonly_handler)


def copy_git_repo(src, dest):
    def app_ignore_pattern(path, names):
        return ['build', '.git', '.gradle', '.idea', '*.idea']
    shutil.copytree(src, dest, ignore=app_ignore_pattern)


def lastest_tag():
    return sh("git describe --tags --abbrev=0")


def gradle_path():
    return 'gradlew' if os.name == 'nt' else './gradlew'


def ensure_repo(origin_url, dirname):
    if os.path.exists(dirname):
        os.chdir(os.path.join(_SOURCE_DIR, dirname))
        print("changed dir to %s"%(os.getcwd()))
        run('git reset --hard HEAD')
        run('git pull --rebase')
    else:
        run("git clone %s"%(origin_url))
        os.chdir(os.path.join(_SOURCE_DIR, dirname))
        print("changed dir to %s"%(os.getcwd()))


def dex2jar_update():
    rawdir = os.getcwd()
    os.chdir(_SOURCE_DIR)
    ensure_repo('https://github.com/pxb1988/dex2jar.git', 'dex2jar')
    os.chdir(os.path.join(_SOURCE_DIR, 'dex2jar'))

    # dex2jar打的"2.0"tag编译不通过，改用最新代码编译。
    # run("git checkout %s"%(lastest_tag()))
    run("%s clean distZip"%(gradle_path()))

    distzipdir = os.path.join('dex-tools', 'build', 'distributions')
    distzips = glob.glob("%s/dex-tools*.zip"%(distzipdir))
    if distzips:
        rmtree(showjar.DEX2JAR)
        rmtree(showjar.CACHE_DIR)
        with zipfile.ZipFile(distzips[0], 'r') as z:
            z.extractall(showjar.CACHE_DIR)
        src = os.path.join(showjar.CACHE_DIR, os.listdir(showjar.CACHE_DIR)[0])
        shutil.move(src, showjar.DEX2JAR)

    os.chdir(rawdir)


def enjarify_update():
    rawdir = os.getcwd()
    os.chdir(_SOURCE_DIR)
    ensure_repo('https://github.com/Storyyeller/enjarify.git', 'enjarify')
    os.chdir(os.path.join(_SOURCE_DIR, 'enjarify'))
    rmtree(showjar.ENJARIFY)
    src = os.path.join(_SOURCE_DIR, 'enjarify')
    copy_git_repo(src, showjar.ENJARIFY)
    # update enjarify.bat中python3为python
    batpath = os.path.join(showjar.ENJARIFY, 'enjarify.bat')
    content = ''
    with open(batpath, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(batpath, 'w', encoding='utf-8') as f:
        content = content.replace('python3 ', 'python ')
        f.write(content)

    os.chdir(rawdir)


def main():
    ensure_dir(_SOURCE_DIR)
    dex2jar_update()
    enjarify_update()


if __name__ == '__main__':
    main()
