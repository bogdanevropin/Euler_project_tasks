import time
from datetime import datetime
print(time.time())

def send_emails():
    for i in range(10*100*100):
        pass
start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
dt3 = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt4 =datetime.fromtimestamp(time.time())
print(dt4)
print(f"{dt4.year}/{dt4.month}/{dt4.day}/{dt4.hour}:{dt4.minute}:{dt4.second}")
print(dt4.strftime("%Y/%m"))

