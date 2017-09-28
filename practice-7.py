import time
import calendar

ticks = time.time()

print("当前时间为：" , ticks)

localtime = time.localtime(time.time())

print("本地时间为：", localtime)


print(time.strftime("%Y-%m-%d %H:%M:%S %Y", time.localtime()))


cal = calendar.month(2017, 9)

print("输出2017年9月份日历：", cal)


cal1 = calendar.monthcalendar(2017, 9)
print(cal1)