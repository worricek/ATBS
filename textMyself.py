#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.
# Preset values:

accountSID = 'some Acct #'
authToken = 'some Auth Token'
myNumber = 'some Mobile number'
twilioNumber = 'some Twilio number'

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
