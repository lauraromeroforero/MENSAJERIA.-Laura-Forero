from twilio.rest import Client 
# Establezco los datos que me dan en twilio como mi ID y mi token y 
#yo soy el mismo cliente con mis datos
account_sid = 'AC5201afc8a15c76025a476d6b59a48971' 
auth_token = '0cafcfa09f557fdd922e0c95bb41a4a0' 
client = Client(account_sid, auth_token) 

#Establezco el mensaje con el numero que me da twilio y el de nosotros 
#registrado en twilio
message = client.messages.create( 
from_='whatsapp:+14155238886',  
body='Viva millos',      
to='whatsapp:+573043576566' 
)

#Por ultimo imprimimos el mensaje para que sea enviado
print(message.sid)