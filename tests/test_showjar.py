# ecoding: utf-8

import shutil
import unittest
import os
import sys
import subprocess
import zipfile
import showjar

TEST_APK = 'test.apk'


def sh(command, print_msg=True):
    p = subprocess.Popen(command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    if print_msg:
        print(result)
    return result


def get_another_apk_path():
    # if os.name == 'nt':
    #     return "d:\\%s"%(TEST_APK)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_cache', TEST_APK)


class Test_emulator_port(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test_emulator_port, cls).setUpClass()
        test_cache = get_another_apk_path()

        showjar._TEST_MODE = True

        global cache_dir
        cache_dir = os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            os.path.pardir,
            showjar._CACHE_DIR))

        global temp_dir
        temp_dir = os.path.abspath(os.path.join(
            cache_dir,
            os.path.splitext(os.path.basename(TEST_APK))[0]))

    @classmethod
    def tearDownClass(cls):
        super(Test_emulator_port, cls).tearDownClass()
        shutil.rmtree(os.path.dirname(get_another_apk_path()))

        showjar._TEST_MODE = False

    def test_apk_name(self):
        showjar.main(TEST_APK)
        jar = os.path.join(temp_dir, 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))


    def test_apk_another_path(self):
        apk_path = get_another_apk_path()
        shutil.copyfile(TEST_APK, apk_path)
        showjar.main(apk_path)
        unzip_cache_dir = os.path.splitext(apk_path)[0]
        self.assertFalse(os.path.exists(os.path.join(unzip_cache_dir, "classes-dex2jar.jar")))
        jar = os.path.join(temp_dir, 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))
        os.remove(apk_path)


    def test_dex_name(self):
        apk_path = TEST_APK
        unzip_cache_dir = os.path.splitext(apk_path)[0]
        with zipfile.ZipFile(apk_path, 'r') as z:
            z.extractall(unzip_cache_dir)
        shutil.copyfile(os.path.join(unzip_cache_dir, 'classes.dex'), 'classes.dex')
        dest_dex = 'classes.dex'
        showjar.main(dest_dex)
        self.assertFalse(os.path.exists(os.path.join(
            unzip_cache_dir, "classes-dex2jar.jar")))
        jar = os.path.join(cache_dir, 'classes', 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))
        shutil.rmtree(unzip_cache_dir)
        os.remove('classes.dex')


    def test_dex_another_path(self):
        apk_path = get_another_apk_path()
        shutil.copyfile(TEST_APK, apk_path)
        unzip_cache_dir = os.path.splitext(apk_path)[0]
        with zipfile.ZipFile(apk_path, 'r') as z:
            z.extractall(unzip_cache_dir)
        dest_dex = os.path.abspath(os.path.join(unzip_cache_dir, 'classes.dex'))
        showjar.main(dest_dex)
        self.assertFalse(os.path.exists(os.path.join(
            unzip_cache_dir, "classes-dex2jar.jar")))
        jar = os.path.join(cache_dir, 'classes', 'classes-dex2jar.jar')
        self.assertTrue(os.path.exists(jar))
        shutil.rmtree(unzip_cache_dir)
        os.remove(apk_path)
