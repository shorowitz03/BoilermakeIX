import smtplib

sender_email = "fluxcache@gmail.com"
receiver_email = "fluxcache@gmail.com"
password = input("Enter a password: ")
message = "This is a test email from python!"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email, receiver_email, message)
print("Email has been sent to ", receiver_email)
