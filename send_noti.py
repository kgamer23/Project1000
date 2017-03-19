#!/usr/bin/env python



# Download the twilio-python library from http://twilio.com/docs/libraries

from twilio.rest import TwilioRestClient



import optparse

import sys

 

# Find these values at https://twilio.com/user/account

account_sid = "AC6f2bc2251e2af868ce6dbe0cdc005c5f"
auth_token = "fb104e099fd011978fcaf91c5ed9421b"

client = TwilioRestClient(account_sid, auth_token)

 

parser = optparse.OptionParser()



parser.add_option('-u', '--sms_url',

    action="store", dest="sms_url",

    help="sms url string", default="spam")



options, args = parser.parse_args()



if options.sms_url == "spam":

  print "**** HEY! You forgot the URL for the SMS: ***"

  print "**** Usage: send_sms -u <URL_string> ***"

  sys.exit()



print '\n\n ************************ SENDING SMS WITH URL: ', options.sms_url ," *************************\n\n"



body_url = "Visitor @FrontDoor: " + options.sms_url

message = client.sms.messages.create(to="(252) 529-8524, from_="(252) 365-5116",

                                     body=body_url)
