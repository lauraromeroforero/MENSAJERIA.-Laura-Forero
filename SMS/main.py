#Importamos twilio message
from email import message
from twilio.rest import Client
import keys

#Definimos el cliente con los datos del key
client = Client(keys.account_sid, keys.auth_token)

#Definimos el cuerpo del mensaje y el destinatario con los numeros de twilio
message = client.messages.create(
    body="Te amo cosita bella",
    from_=keys.twilio_number,
    to=keys.target_number
)

#Imprimimos para que el mensaje sea envia
print(message.body)