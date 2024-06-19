#Codigo para la automatizacion de envios de e-mails

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



your_email = 'Ingrese el mail a utilizar'
your_password = 'wvus oork tzmk uezl'

recipent = 'Ingrese el mial del destinatario'

message = MIMEMultipart()
message['From'] = your_email
message['To'] = recipent
message['Subject'] = 'Email de agradecimiento'

body = 'Gracias por estar siempre te amo con todo el corazon!!!!!'
message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('SMTP.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipent, message.as_string())
smtp_server.quit()
print('Email Enviado!!')
