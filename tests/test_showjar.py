# ecoding: utf-8

import shutil
import unittest
import os
import subprocess
import zipfile
import showjar
import sys
import fnmatch


TEST_APK = 'test.apk'


def sh(command, print_msg=True):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    if print_msg:
        print(result)
    return result


def get_another_apk_path():
    test_cache = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'test_cache')
    if not os.path.exists(test_cache):
        os.makedirs(test_cache)
    return os.path.join(test_cache, TEST_APK)


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


class Test_emulator_port(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test_emulator_port, cls).setUpClass()

        global cache_dir
        cache_dir = os.path.abspath(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), os.path.pardir,
                showjar.CACHE_DIR))

        global temp_dir
        temp_dir = os.path.abspath(
            os.path.join(cache_dir,
                         os.path.splitext(os.path.basename(TEST_APK))[0]))

    @classmethod
    def tearDownClass(cls):
        super(Test_emulator_port, cls).tearDownClass()
        shutil.rmtree(os.path.dirname(get_another_apk_path()), True)

    def test_apk_name(self):
        sh("python showjar.py -e dex2jar -t 1 %s"%(TEST_APK))
        jar = os.path.join(temp_dir, 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))

    def test_apk_another_path(self):
        apk_path = get_another_apk_path()
        shutil.copyfile(TEST_APK, apk_path)
        sh("python showjar.py -e dex2jar -t 1 %s"%(apk_path))
        print(apk_path)
        unzip_cache_dir = os.path.splitext(apk_path)[0]
        self.assertFalse(
            os.path.exists(
                os.path.join(unzip_cache_dir, "classes-dex2jar.jar")))
        jar = os.path.join(temp_dir, 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))
        os.remove(apk_path)

    def test_apk_with_res_another_path(self):
        apk_path = get_another_apk_path()
        shutil.copyfile(TEST_APK, apk_path)
        sh("python showjar.py -r 1 -e dex2jar -t 1 %s"%(apk_path))
        unzip_cache_dir = os.path.splitext(apk_path)[0]
        self.assertFalse(
            os.path.exists(
                os.path.join(unzip_cache_dir, "classes-dex2jar.jar")))
        jar = os.path.join(temp_dir, 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))
        os.remove(apk_path)

    def test_dex_name(self):
        apk_path = TEST_APK
        unzip_cache_dir = os.path.splitext(apk_path)[0]
        with zipfile.ZipFile(apk_path, 'r') as z:
            z.extractall(unzip_cache_dir,)
        shutil.copyfile(
            os.path.join(unzip_cache_dir, 'classes.dex'), 'classes.dex')
        dest_dex = 'classes.dex'
        sh("python showjar.py -e dex2jar -t 1 %s"%(dest_dex))
        self.assertFalse(
            os.path.exists(
                os.path.join(unzip_cache_dir, "classes-dex2jar.jar")))
        jar = os.path.join(cache_dir, 'classes', 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))
        shutil.rmtree(unzip_cache_dir,)
        os.remove('classes.dex')

    def test_dex_another_path(self):
        apk_path = get_another_apk_path()
        shutil.copyfile(TEST_APK, apk_path)
        unzip_cache_dir = os.path.splitext(apk_path)[0]
        with zipfile.ZipFile(apk_path, 'r') as z:
            z.extractall(unzip_cache_dir)
        dest_dex = os.path.abspath(
            os.path.join(unzip_cache_dir, 'classes.dex'))
        sh("python showjar.py -e dex2jar -t 1 %s"%(dest_dex))
        jar = os.path.join(cache_dir, 'classes', 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))
        shutil.rmtree(unzip_cache_dir)
        os.remove(apk_path)

    def test_enjarify(self):
        if sys.version_info < (3, 5):
            print("enjarify only support python3")
            return
        apk_path = get_another_apk_path()
        shutil.copyfile(TEST_APK, apk_path)
        cache = os.path.dirname(apk_path)
        output_file = os.path.join(cache, "%s-enjarify.jar" %
                                   (os.path.splitext(os.path.basename(apk_path))[0]))
        sh("python showjar.py -e enjarify -o %s -t 1 %s"%(cache, apk_path))
        self.assertTrue(os.path.exists(output_file))
        if os.path.exists(cache):
            shutil.rmtree(cache, True)

    def test_cfr(self):
        apk_path = get_another_apk_path()
        shutil.copyfile(TEST_APK, apk_path)
        cache = os.path.dirname(apk_path)
        outputdir = os.path.join(cache, os.path.splitext(os.path.basename(apk_path))[0])
        sh("python showjar.py -e cfr -o %s -t 1 %s"%(cache, apk_path))
        for f in find_files(outputdir, "*.java"):
            self.assertTrue(f)
            break
        if os.path.exists(cache):
            shutil.rmtree(cache, True)
