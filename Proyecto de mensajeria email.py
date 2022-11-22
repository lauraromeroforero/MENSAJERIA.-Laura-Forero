import os
from email.message import EmailMessage
import ssl
import smtplib

email_emisor = 'en17la@gmail.com'
email_contrasena = 'piscdattqdcmojci'
#prueba con mas de dos correos
email_receptor = 'yuliysandrita123@gmail.com', 'contrekalo@gmail.com', 'en17la@gmail.com', 'forero0801laura@gmail.com', 'minnielaura27@gmail.com'

cuerpo = """
Si se pudo Profesor Hugo Ruiz PRUEBA 2 \n ATT:Laura Lorena Forero Romero
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
