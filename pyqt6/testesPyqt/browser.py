import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText


login = "erickjb93@gmail"
senha = "zrzhokxrkyzslcgd"
port = "587"
host = "smtp.gmail.com"

servidor = smtplib.SMTP(host, port)

servidor.starttls()
servidor.ehlo()

servidor.login(login, senha)

msg = MIMEMultipart()
msg["From"] = "erickjb93@gmail.com"
msg["To"] = "mowengine1228@gmail.com"
msg["Subject"] = "Aviso"
corpo = "ola, tudo bom"

msg.attach(MIMEText(corpo,"plain"))

servidor.sendmail(msg["From"], msg["To"], msg.as_string())
servidor.quit()
