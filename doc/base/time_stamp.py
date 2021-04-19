# 使用time
import time, datetime

timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print(otherStyleTime)   # 2013--10--10 23:40:00
# 使用datetime
timeStamp = 1381419600
dateArray = datetime.datetime.fromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
print(otherStyleTime)   # 2013--10--10 23:40:00
# 使用datetime，指定utc时间，相差8小时
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
print(otherStyleTime)   # 2013--10--10 15:40:00

print("******************************")
localTime = datetime.datetime.now()
print("type_localTime", type(localTime))
if isinstance(localTime, datetime.datetime):
    print("localTime", localTime)

if __name__ == '__main__':
    current_time = datetime.datetime.now()
    print("time", current_time.strftime("%Y-%m-%d %H:%M:%S"))


