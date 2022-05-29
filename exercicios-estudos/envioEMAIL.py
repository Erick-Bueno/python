from http import server
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

codigo = random.randint(100,999)

comprador = "mowengine1228@gmail.com"

host = "smtp.gmail.com"
port = "587"
usuario = "erickjb93@gmail.com"
senha = "zrzhokxrkyzslcgd"

servidor = smtplib.SMTP(host, port)

servidor.ehlo()
servidor.starttls()

servidor.login(usuario, senha)

corpo = f"seu codigo é {codigo}"
msg_email = MIMEMultipart() #um email é codificado em mimemultipart
msg_email["From"] = usuario
msg_email["To"] = comprador
msg_email["Subject"] = "Codigo de confirmação"
msg_email.attach(MIMEText(corpo, 'plain'))#o conteudo do email é um texto normal 

servidor.sendmail(msg_email["From"],msg_email["To"],msg_email.as_string())

servidor.quit()
