import email, smtplib, ssl
from re import L
from providers import PROVIDERS
import time
# used for MMS
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from os.path import basename

global email_list, phone_list, carrier_list


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


def main():
    number = input("number: ")
    provider = input("provider: ")
    sender_credentials = ("fluxcache@gmail.com", "bernardogarrettmikeyronsam")
    message = input("message: ")
    send_sms_via_email(number, message, provider, sender_credentials)
    print("Success!")


if __name__ == "__main__":
    main()

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

