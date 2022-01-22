# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['AC4d8d893f0532a1f770ab6ee5d68b0b7e']
auth_token = os.environ['3b2cec1b882ebe0cf9aa58163eb084ca']

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12167040467",
    from_="+16077033084",
    body="Hello there!")
