#Importamos twilio message
from email import message
from twilio.rest import Client
import keys

#Definimos el cliente con los datos del key
client = Client(keys.account_sid, keys.auth_token)