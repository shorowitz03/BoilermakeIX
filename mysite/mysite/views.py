from django.http import HttpResponse
from django.shortcuts import render
import cgi, cgitb

form = cgi.FieldStorage()

# Each function is a page that must be called in urls.py with 
# views.name with "modifier/"

# Bar functions
def index(request):
   return render(request, 'index.html') # Third variable can be data

def trends(request):
    return render(request, 'MarketTrends.html')

def about_us(request):
    return render(request, 'about_us.html')

email_list = []
phone_list = []
carrier_list = []
def contacts(request):

    # Get phone numbers
    phone_list.append(request.GET.get('phone number'))

    # Get carriers
    carrier_list.append(request.GET.get('carrier'))

    # Get emails
    email_list.append(request.GET.get('email'))

    return render(request, 'contact.html')

def redirect(self):
    textMain()

# Cloud functions

def fourofour(request):
    return render (request, '404.html')

# Stock functions

def tesla(request):
    return render(request, 'template.html')





def viewpara(request):
    current_user = request.user.get_username()
    return render(request, 'dataPage.html',{'user': current_user})



# Providers.py import
PROVIDERS = {
    "AT&T": {"sms": "txt.att.net", "mms": "mms.att.net", "mms_support": True},
    "Boost Mobile": {
        "sms": "sms.myboostmobile.com",
        "mms": "myboostmobile.com",
        "mms_support": True,
    },
    "C-Spire": {"sms": "cspire1.com", "mms_support": False},
    "Cricket Wireless": {
        "sms": "sms.cricketwireless.net ",
        "mms": "mms.cricketwireless.net",
        "mms_support": True,
    },
    "Consumer Cellular": {"sms": "mailmymobile.net", "mms_support": False},
    "Google Project Fi": {"sms": "msg.fi.google.com", "mms_support": True},
    "Metro PCS": {"sms": "mymetropcs.com", "mms_support": True},
    "Mint Mobile": {"sms": "mailmymobile.net", "mms_support": False},
    "Page Plus": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
    "Republic Wireless": {
        "sms": "text.republicwireless.com",
        "mms_support": False,
    },
    "Sprint": {
        "sms": "messaging.sprintpcs.com",
        "mms": "pm.sprint.com",
        "mms_support": True,
    },
    "Straight Talk": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
    "T-Mobile": {"sms": "tmomail.net", "mms_support": True},
    "Ting": {"sms": "message.ting.com", "mms_support": False},
    "Tracfone": {"sms": "", "mms": "mmst5.tracfone.com", "mms_support": True},
    "U.S. Cellular": {
        "sms": "email.uscc.net",
        "mms": "mms.uscc.net",
        "mms_support": True,
    },
    "Verizon": {"sms": "vtext.com", "mms": "vzwpix.com", "mms_support": True},
    "Virgin Mobile": {
        "sms": "vmobl.com",
        "mms": "vmpix.com",
        "mms_support": True,
    },
    "Xfinity Mobile": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
}


# Text Messenger.py import
import email, smtplib, ssl
from re import L
import time
# used for MMS
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from os.path import basename


def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)


def textMain():
   
    # Define initial messages
    sender_credentials = ("fluxcache@gmail.com", "bernardogarrettmikeyronsam")
    initial_message = "Thank you for signing up for Flux Cache!"
    update_message = "Flux Cache has a stock update:"
    stock_message = "Default has gone below n dollars"
    
    # Initial message
    for j in range(len(phone_list)):
        number_text = phone_list[j]
        provider = carrier_list[j]
        send_sms_via_email(number_text, initial_message, provider, sender_credentials)

    # Update message
    for i in range(len(phone_list)):
        number_text = phone_list[i]
        provider = carrier_list[i]
        send_sms_via_email(number_text, update_message, provider, sender_credentials)
        send_sms_via_email(number_text, stock_message, provider, sender_credentials)


    print("Success!")\


########################################################################

#def send_mms_via_email(
#    number: str,
#    message: str,
#    file_path: str,
#    mime_maintype: str,
#    mime_subtype: str,
#    provider: str,
##    sender_credentials: tuple,
#    subject: str = "sent using etext",
#    smtp_server: str = "smtp.gmail.com",
#    smtp_port: int = 465,
#):
#
#    sender_email, email_password = sender_credentials
#    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'##

#    email_message=MIMEMultipart()
#    email_message["Subject"] = subject
#    email_message["From"] = sender_email
#    email_message["To"] = receiver_email#
#
 #   email_message.attach(MIMEText(message, "plain"))
#
 #   with open(file_path, "rb") as attachment:
  #      part = MIMEBase(mime_maintype, mime_subtype)
   #     part.set_payload(attachment.read())
#
 #       encoders.encode_base64(part)
  #      part.add_header(
   #         "Content-Disposition",
    #        f"attachment; filename={basename(file_path)}",
     #   )

 #       email_message.attach(part)

#    text = email_message.as_string()

    #with smtplib.SMTP_SSL(
   #     smtp_server, smtp_port, context=ssl.create_default_context()
  #  ) as email:
 #       email.login(sender_email, email_password)
#        email.sendmail(sender_email, receiver_email, text)

