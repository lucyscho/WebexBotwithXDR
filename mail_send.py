from webex_bot.models.command import Command
import sys
import os
import requests
import smtplib, ssl

class Send_Email(Command):
    def __init__(self):
        super().__init__(
            command_keyword='send_email',
        )

    def execute(self, message, attachment_actions, activity):
        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email = ",xyz@cisco.com"
        receiver_email = ",xyz@cisco.com"
        message = "test email"
        password = 'passwrd23!'

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email    
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit() 
        
        server.sendmail(sender_email, receiver_email, message)



