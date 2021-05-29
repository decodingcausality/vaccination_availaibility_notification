"""
Purpose :   Module to trigger SMS notification
Input   :
"""

from twilio.rest import Client
import config

def send(age_group, pin_code,address) :


    body = f"Available vaccine for age group : {age_group} , PIN CODE : {pin_code} at {address}"

    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token = config.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.api.account.messages.create(
             body= body,
             from_= config.source_mobile_number,
             to= config.target_mobile_number
         )
    print(f" message : {message.status}")
    return message
