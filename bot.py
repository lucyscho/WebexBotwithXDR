from webex_bot.webex_bot import WebexBot
from webex_bot.commands.echo import EchoCommand
from mail_send import Send_Email
from webex_bot.models.command import Command
import os
import requests
from webexteamssdk import WebexTeamsAPI
import pandas


wbx_token = 'NDE2YjZhM2MtZDY1Mi00NjI4LTk3ZWYtN2VhODgxNDQwYmY2YmEyMDgwYmUtZWY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

bot = WebexBot(wbx_token,
               approved_domains='cisco.com')

bot.add_command(Send_Email())

df = pandas.read_csv('Responses.csv', skiprows=1)
recipient_emails = df.iloc[:,1]

api_access_token = 'NDE2YjZhM2MtZDY1Mi00NjI4LTk3ZWYtN2VhODgxNDQwYmY2YmEyMDgwYmUtZWY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
message_text = "Hello! Our record indicate that you have been a victim of a phishing attack. [HACKATHON PROOF OF CONCEPT]\n https://www.cisco.com/c/en/us/products/security/email-security/what-is-phishing.html"

api = WebexTeamsAPI(access_token=api_access_token)

for recipient_email in recipient_emails:
    api.messages.create(toPersonEmail=recipient_email, text=message_text)

bot.run()





