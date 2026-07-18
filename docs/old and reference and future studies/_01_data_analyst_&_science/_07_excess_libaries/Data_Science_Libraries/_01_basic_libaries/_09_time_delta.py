from datetime import datetime,timedelta

d1=datetime(2024,1,1)
d2=datetime.now()

d=d2-d1
print(d)

print("days",d.days)
print("micro",d.microseconds)
print("sec",d.seconds)
print("t sec",d.total_seconds())

print()

d3=datetime(1996,8,19)+timedelta(days=100,seconds=1)

print(d3)