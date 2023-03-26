#!/usr/bin python3
# library update helper

import subprocess
import shutil
import stat
import os
import glob
from typing import Tuple
import zipfile
import showjar
import urllib.request
import json
import re
from datetime import datetime, timedelta


_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
_SOURCE_DIR = os.path.join(_ROOT_PATH, 'sources')

_last_update_time = datetime.now()


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
        if os.path.isdir(path):
            shutil.rmtree(path, onerror=readonly_handler)
        else:
            os.remove(path)


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


def download_file(url, store_path):
    print("found download url: %s, download file to: %s"%(url, store_path))

    def reporthook(a, b, c):
        print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")
    try:
        if url.lower().startswith('http'):
            urllib.request.urlretrieve(url, store_path, reporthook=reporthook)
        else:
            raise ValueError from None
        if not os.path.exists(store_path):
            print("download file failed: %s"%(store_path))
            return False
    except Exception as e:
        print("download file error:")
        print(e)
    return True


def download_release(repo_owner, repo_name, last_update_time, refile, destpath):
    """download lastest release file from github"""
    url = "https://api.github.com/repos/%s/%s/releases/latest"%(repo_owner, repo_name)
    try:
        print("download_release: %s/%s, min_publish_time: %s, destpath: %s"
              % (repo_owner, repo_name, last_update_time, destpath))
        response = ''
        if url.lower().startswith('http'):
            with urllib.request.urlopen(url) as connection:
                response = json.loads(connection.read().decode('utf-8'))
        else:
            raise ValueError from None
        publish_time = datetime.strptime(response['published_at'], '%Y-%m-%dT%H:%M:%SZ')
        # debug
        # publish_time = datetime.strptime('2023-02-20T11:33:37Z', '%Y-%m-%dT%H:%M:%SZ')
        print("min_publish_time: %s, repo publish time: %s"%(str(last_update_time), str(publish_time)))
        if publish_time.timetuple() <= last_update_time.timetuple():
            print("ignore update '%s/%s'"%(repo_owner, repo_name))
            return
        browser_download_url = ''
        for asset in response['assets']:
            browser_download_url = asset['browser_download_url']
            if re.search(refile, browser_download_url):
                break
        if not browser_download_url:
            print("can not find download url %s/%s"%(repo_owner, repo_name))
            return
        store_path = os.path.join(_SOURCE_DIR, os.path.basename(browser_download_url))
        if not download_file(browser_download_url, store_path):
            return

        # # unzip file
        rmtree(showjar.CACHE_DIR)
        if store_path.endswith('.zip'):
            with zipfile.ZipFile(store_path, 'r') as z:
                z.extractall(showjar.CACHE_DIR)
            overwrite_tree(showjar.CACHE_DIR, destpath)
        else:
            destpath2 = destpath
            if os.path.isdir(destpath):
                destpath2 = os.path.join(destpath, os.path.basename(store_path))
            shutil.copyfile(store_path, destpath2)

    except Exception as e:
        print("download release error:")
        print(e)


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
    # webbrowser.open_new_tab("https://github.com/skylot/jadx/releases")
    download_release('skylot', 'jadx', _last_update_time, r'jadx-\d.+\.zip', showjar.JADX)

    rawdir = os.getcwd()
    os.chdir(showjar.JADX)

    # remove unused files
    rmtree('README.md')
    rmtree('NOTICE')
    rmtree('LICENSE')

    # update jadx script config, fix issues #7.
    def update_jvm_opts(script_path):
        script_path = os.path.abspath(script_path)
        if not script_path.startswith(showjar.JADX):
            return
        print("update_jvm_opts: %s"%(script_path))
        content = ''
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('"-XX:MaxRAMPercentage=70.0"', '')
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(content)

    update_jvm_opts('bin/jadx')
    update_jvm_opts('bin/jadx-gui')
    update_jvm_opts('bin/jadx-gui.bat')
    update_jvm_opts('bin/jadx.bat')

    os.chdir(rawdir)


def apktool_updater():
    print("---------------------------apktool_updater start---------------------------")
    # webbrowser.open_new_tab("https://ibotpeaches.github.io/Apktool/")
    download_release('iBotPeaches', 'Apktool', _last_update_time, r'apktool-\d.+\.jar', showjar.APKTOOL)


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


def initEnv():
    ensure_dir(_SOURCE_DIR)

    global _last_update_time
    readme_path = os.path.join(_ROOT_PATH, 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        datestring = re.search(r"update\sat\s(\d+-\d+-\d+)", content)
        _last_update_time = datetime.strptime(datestring.group(1), '%Y-%m-%d')

    # debug code
    _last_update_time = _last_update_time - timedelta(days=0)
    print("last update time: %s"%(_last_update_time))


def main():
    initEnv()
    # enjarify_updater()
    # dex2jar_updater()
    # jadx_updater()
    apktool_updater()
    # fernflower_updater()


if __name__ == '__main__':
    main()
