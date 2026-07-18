from twilio.rest import Client

import _08_excess_libaries.Data_Science_Libraries._02_advanced_libaries._03_text_sms.config as config

import random
client=Client(config.acc,config.token)
otp = ''.join(random.choices('0123456789', k=4))
# print("Generated OTP:", otp)

client.messages.create(
    to="+918807796595",
    from_="+15736724620",
    body=otp,
)

if otp==input("enter your otp"):
    print("otp verified")
else:
    print("wrong otp")

