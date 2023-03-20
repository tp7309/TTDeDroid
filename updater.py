#!/usr/bin python3
# library update helper

import subprocess
import shutil
import stat
import os
import glob
from typing import Tuple
import zipfile
import webbrowser
import showjar


_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
_SOURCE_DIR = os.path.join(_ROOT_PATH, 'sources')


def sh(command, print_msg=True):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    bytes_result = p.stdout.read()
    try:
        result = bytes_result.decode('utf-8')
    except Exception:
        # fix some window system error
        result = bytes_result.decode('gbk')
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
    app_ignore = shutil.ignore_patterns('build', '.git', '.gradle', '.idea', '*.idea')
    overwrite_tree(src, dest, ignore=app_ignore)


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
        run("git clone --depth=1 %s"%(origin_url))
        os.chdir(os.path.join(_SOURCE_DIR, dirname))
        print("changed dir to %s"%(os.getcwd()))


def overwrite_tree(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                overwrite_tree(os.path.join(src, f),
                               os.path.join(dest, f),
                               ignore)
    else:
        shutil.copyfile(src, dest)


def dex2jar_updater():
    print("---------------------------dex2jar_updater start---------------------------")
    rawdir = os.getcwd()
    os.chdir(_SOURCE_DIR)
    ensure_repo('https://github.com/pxb1988/dex2jar.git', 'dex2jar')
    os.chdir(os.path.join(_SOURCE_DIR, 'dex2jar'))

    run("git checkout 2.x")
    run("%s clean distZip"%(gradle_path()))

    distzipdir = os.path.join('dex-tools', 'build', 'distributions')
    distzips = glob.glob("%s/dex-tools*.zip"%(distzipdir))
    if distzips:
        rmtree(showjar.CACHE_DIR)
        with zipfile.ZipFile(distzips[0], 'r') as z:
            z.extractall(showjar.CACHE_DIR)
        src = os.path.join(showjar.CACHE_DIR, os.listdir(showjar.CACHE_DIR)[0])
        overwrite_tree(src, showjar.DEX2JAR)
    os.chdir(rawdir)


def enjarify_updater():
    print("---------------------------enjarify_updater start---------------------------")
    rawdir = os.getcwd()
    os.chdir(_SOURCE_DIR)
    ensure_repo('https://github.com/Storyyeller/enjarify.git', 'enjarify')
    os.chdir(os.path.join(_SOURCE_DIR, 'enjarify'))
    src = os.path.join(_SOURCE_DIR, 'enjarify')
    copy_git_repo(src, showjar.ENJARIFY)
    # delete tests/
    rmtree(os.path.join(showjar.ENJARIFY, 'tests'))
    # 升级enjarify.bat中python3为python
    batpath = os.path.join(showjar.ENJARIFY, 'enjarify.bat')
    content = ''
    with open(batpath, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(batpath, 'w', encoding='utf-8') as f:
        content = content.replace('python3 ', 'python ')
        content = content.replace('py -3 ', 'python ')
        f.write(content)

    os.chdir(rawdir)


def jadx_updater():
    print("---------------------------jadx_updater start---------------------------")
    webbrowser.open_new_tab("https://github.com/skylot/jadx/releases")


def apktool_updater():
    print("---------------------------apktool_updater start---------------------------")
    webbrowser.open_new_tab("https://ibotpeaches.github.io/Apktool/")


def fernflower_updater():
    print("---------------------------fernflower_updater start---------------------------")
    rawdir = os.getcwd()
    os.chdir(_SOURCE_DIR)
    maven_version = sh("mvn -v")
    if "not found" in maven_version or "无法将" in maven_version:
        print("please configure maven first!")
        return
    ensure_dir(os.path.join(_SOURCE_DIR, 'fernflower'))
    os.chdir(os.path.join(_SOURCE_DIR, 'fernflower'))
    run("mvn dependency:get -DrepoUrl=https://www.jetbrains.com/intellij-repository/releases/ \
    -Dartifact=com.jetbrains.intellij.java:java-decompiler-engine:LATEST -Ddest=.")
    jars = glob.glob("%s/%s" % (os.getcwd(), "java-decompiler-engine*.jar"))
    if not jars:
        print("expected jar is not found!")
        return
    jar = jars[0]
    print("latest jar: %s"%(jar))
    shutil.copyfile(jar, showjar.fernflowerpath())
    os.chdir(rawdir)


def main():
    ensure_dir(_SOURCE_DIR)
    enjarify_updater()
    dex2jar_updater()
    jadx_updater()
    apktool_updater()
    fernflower_updater()


if __name__ == '__main__':
    main()
