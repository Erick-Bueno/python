import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


login = "erickjb93@gmail.com"
senha = "zrzhokxrkyzslcgd"
host = "smtp.gmail.com"
port = "587"

servidor = smtplib.SMTP(host,port)

servidor.ehlo()
servidor.starttls()

servidor.login(login, senha)

msg = MIMEMultipart()
msg['From'] = login
msg['To'] = "mowengine1228@gmail.com"
msg['subject'] = "mensagem de erick"

corpo = "ola, bom dia"

msg.attach(MIMEText(corpo, "plain"))

servidor.sendmail(msg["From"], msg["To"], msg.as_string())
servidor.quit()