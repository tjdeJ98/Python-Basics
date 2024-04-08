import time
from datetime import datetime

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()  # cur datetime
# For parsing or converting datetime string
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print(dt2 > dt1)
