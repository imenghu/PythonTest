#! /usr/bin/python
# version 1.1

import sys
import os
import time
import datetime

# 要备份的文件夹目录
fileFolder = r'D:\BPM'


# 要输出的文件名称(默认压缩在脚本执行的文件夹下)
# 需要自己在服务器上创建好fileName的目录
fileName = r'D:\Backup'  # 修改成存放备份的目录并在服务器上建立好。
fileName += r'\BPM_bak_' + time.strftime('%Y%m%d%H') + '.zip'

# winrar a -r d:\scon.zip c:\scon  将c盘scon文件夹下的所有文件生成压缩并移动到d盘的目录下
exeCode = 'WinRAR a -r  %s %s' % (fileName, fileFolder)

# 备份日志
filebak_log = r"D:\Backup\filebak.log"


def work():
    print('----开始备份----')
    if os.system(exeCode) == 0:
        print('----备份完成----' + time.strftime('%Y%m%d%H'))
        with open(filebak_log, 'a') as filebak:
            filebak.write('successfull backup to %s \n' % fileName)


def main(day, hour, minute):
    print('工具启动')
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == hour and now.minute == minute and now.day == day:
                break
        work()
        time.sleep(180)


main(19, 12, 30)
