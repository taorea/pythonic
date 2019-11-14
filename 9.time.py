import time
datatime = time.time()
print(datatime)
int_time = int(datatime)
print(int_time)
hour = int_time / 3600
print(hour)
second = int_time % 3600
day = hour / 24
year = day / 365
print("year:{0} day:{1} hour:{2} seocond:{3}".format(year,day,hour,second))