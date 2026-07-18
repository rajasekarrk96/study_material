import random
import string

print(random.random())

print(random.randint(1,10))

print(random.choice([1,2,3,4,5]))
l=["1",'2','3','4','5','6']
p="-".join(l)
print(p)

p="sadjkfsdjkfhgsad"
p=p.split("s")
print(p)

print(random.choices("1234567890",k=4))
print("".join(random.choices("1234567890",k=4)))

print(string.ascii_letters)

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.printable)
print(list(string.punctuation))
l=[1,2,3,4,5,6,7]
random.shuffle(l)
print(l)