#go to twilio site and sign up with mail and phone number
#+15736724620

from twilio.rest import Client

#can hide api and important information by hiding it in file called config.py
#then create file named .gitignore and mention the config.py in it
#once it has been added it will not reflect it github repository.

import _08_excess_libaries.Data_Science_Libraries._02_advanced_libaries._03_text_sms.config as config

client=Client(config.acc,config.token)

client.messages.create(
    to="+918807796595",
    from_="+15736724620",
    body="checking",
)

