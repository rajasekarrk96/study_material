from datetime import datetime
import time

d=datetime(1996, 8,19)
print(d)

d=datetime.now()
print(d)

d=d.strptime("1996/08/19","%Y/%m/%d")
print(d)

# can view diretives in the link bottom
# https://docs.python.org/3/library/datetime.html

d=datetime.fromtimestamp(time.time())
print(d)

print(f"{d.year}/{d.month}")
m=f"{d.year}/{d.month}"
d=d.strftime("%Y/%m")
print(d)
print(d==m)