from twilio.rest import Client

accountSID = 'some account ID'
authToken = 'some Auth Token'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = 'some Twilio number'
myCellPhone = 'some Mobile Number'

message = twilioCli.messages.create(body='Mr. Watson - \
Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
