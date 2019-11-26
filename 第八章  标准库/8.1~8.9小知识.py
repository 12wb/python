'''
# [案例8.1] 测试datetime模块里的datetime类基本功能   P147
from datetime import datetime,date,time
print(datetime.now())  # 返回当天的日期和时间，datetime类型（1）
today = datetime.now()  # 定义today为当天的日期时间对象
print(datetime.date(today))  # 返回today当天的日期对象，date类型（2）
print(datetime.time(today))  # 返回today当天的时间对象，time类型（2）
print(datetime.ctime(today))  # 返回"星期，月，日，时，分，秒，年"格式的字符串（4）
print(datetime.utcnow())  # 返回当前的UTC日期和时间，datetime类型（5）
print(datetime.timestamp(today))  # 返回当前的时间戳(UNIX时间戳)，浮点数类型（6）
print(datetime.utcfromtimestamp(datetime.timestamp(today)))  # 根据时间戳返回UTC日期时间，datetime类型（7）
date1 = date(2018,2,12)  # 使用date类，实现实例date1对象
time1 = time(20,53,48)  # 使用time类，实现实例time1对象
print(datetime.combine(date1,time1))  # 绑定日期、时间，生成新的datetime对象（8）
newDatetime = datetime.strptime("12/2/18 20:59",'%d%m%y%H:%M')  # 用字符串和指定格式生成新的datetime对象
print(newDatetime)  # 打印新的datetime对象（9)
for tv in datetime.timetuple():  # 把today当作时间元组，循环打印（10）
    print(tv)
print(today.isocalendar())  # ISO格式的日期（11）
print(today.strftime("%Y年%m月%d日%H:%M:%S%p"))  # 对datetime对象自定义格式，返回字符串类型的值（12）
'''


import os
print(os.environ)  # 获取操作系统里设置的环境变量
print(os.getcwd())  # 返回表示当前工作路径的字符串
print(os.system('ping 127.0.0.1'))  # 函数在子shell中执行命令
print(os.urandom(10))  # 执行加密随机函数


import sys
print(sys.platform)  # 获取操作系统标识符
print(sys.getwindowsversion())  # 执行获取Windows的版本型号






