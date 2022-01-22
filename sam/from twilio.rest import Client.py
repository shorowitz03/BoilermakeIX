from twilio.rest import Client 
 
account_sid = 'ACc8f3a958aa33e2049c0e6b44afb5d614' 
auth_token = '[6eab447ca990410a3854502eb88c16de]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGade2f204c9601b37f1056b53b07df553', 
                              body='Hey',      
                              to='+12167040467' 
                          ) 
 
print(message.sid)