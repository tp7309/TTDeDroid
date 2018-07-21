#!/user/bin/python3
import datetime
import time
import subprocess
import random
import os


APP_ID = 'com.pptv.tvsports.dev'


def run(command):
    print(command + '...')
    subprocess.call(command, shell=True)


def apply_test_snsdk():
    """"测试苏宁sdk启动日志上报"""
    repeat_time = 10
    wait_times = [0, 3, 5, 10, 45, 80]
    uris = [
        'pptv_tvsports://tvsports_diy?from_internal=1'
    ]
    run("adb shell am force-stop %s" % (APP_ID))
    print("start time: " + str(datetime.datetime.now()))

    uri_index = 0

    def nexturi(uri_index):
        return uris[uri_index]
        # uri_index = 1 if uri_index == 0 else 0
        # return uris[uri_index]

    for i in range(0, repeat_time):
        print("%sindex: %d" % (os.linesep, i + 1))
        run('adb shell am start -a "android.intent.action.VIEW" -d "%s"' %
            (nexturi(uri_index)))
        wait_time = wait_times[random.randint(0, len(wait_times) - 1)]
        print("wait %ds..." % (wait_time))
        if wait_time == 0:
            run("adb shell am force-stop %s" % (APP_ID))
        else:
            time.sleep(wait_time)
        run('adb shell input keyevent 4')  # KEYCODE_BACK
        time.sleep(5)  # 每次启动间隔5秒


apply_test_snsdk()