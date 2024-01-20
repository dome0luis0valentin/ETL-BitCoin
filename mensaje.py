# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC608cb760f5502e2a169e216f89beda92'
auth_token = '4b8638b15b988893fdd86a626fc95023'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+5493455532221'
                          )

print(message.sid)
