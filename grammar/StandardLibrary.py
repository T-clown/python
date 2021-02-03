import glob
import os
import shutil

# 返回当前的工作目录
import sys
import time
from datetime import date
from urllib.request import urlopen

print(os.getcwd())
# 修改当前的工作目录
# os.chdir('/server/accesslogs')
# 执行系统命令 mkdir
# os.system('mkdir today')

# dir(os)

# help(os)


# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

print(glob.glob('*.py'))

print(sys.argv)

# 大多脚本的定向终止都使用 "sys.exit()"。

print('tea for too'.replace('too', 'two'))

for line in urlopen('https://www.runoob.com/python3/python3-stdlib.html'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print(line)

today=date.today()
print(today)

print(today.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
#datetime转时间戳
print(int(time.mktime(today.timetuple())))
print(time.time())
#当前时间戳 time_stamp = time.time()
#时间戳转datetime datetime.datetime.fromtimestamp(time_stamp)