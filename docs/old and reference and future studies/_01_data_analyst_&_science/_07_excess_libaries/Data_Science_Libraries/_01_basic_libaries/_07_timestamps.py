import time
from decimal import Decimal

print(time.time()) # time mentioned in seconds from the start of the epoch
j=0
def send_email():
    global j  # Declare 'j' as a global variable to modify it within the function
    for i in range(10000):
        j=j+1

s = time.time()
send_email()
e = time.time()

d = Decimal(str(e - s))  # Convert the float difference to string first, then to Decimal
print(d)
