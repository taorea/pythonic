#从1970年1月1日零时开始所经过的时间
import time
currentTime = time.time()
print(currentTime)
#获取总秒数
totalSeconds = int(currentTime)
print("totalSeconds:",totalSeconds)
totalMinutes = totalSeconds // 60
currentsecond = totalSeconds % 60
totalHours = totalMinutes // 60
currentMinute = totalMinutes % 60
totalDays = totalHours // 24
currentHours = totalHours % 24
totalyears = totalDays // 365
print('''
from 1970 now is :
years:%20s
hour:%20s 
minutes:%20s 
second %20s '''%(totalyears,currentHours,currentMinute,currentsecond))