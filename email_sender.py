from email.message import EmailMessage
import ssl
import smtplib
import re



sender = input(" sender ")
receiver = input("receiver ")
mail_password  = "iseiocxgwtvdqnfc"
topic = input("topic ")
content = input("content ")
notlogin = True





###########################################################################


def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(email_pattern, email)
    return bool(match)

############################################################################


while notlogin:
    
    if is_valid_email(sender):
        notlogin = False
    
    else :
        print(" input a valid email ")
        sender = input(" enter youe email ")
        mail_password  = "iseiocxgwtvdqnfc"
        is_valid_email(sender)

############################################################################


mail = EmailMessage()
mail["From"] = sender
mail["to"]  = receiver
mail["subject"] = topic
mail.set_content(content)

context = ssl.create_default_context()

with smtplib.SMTP_SSL ("smtp.gmail.com" , 465  , context = context ) as smtp:
    smtp.login(sender , mail_password)
    smtp.sendmail(sender , receiver , mail.as_string())

###########################################################################




