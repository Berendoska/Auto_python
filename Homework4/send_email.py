import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromwhome = "fromtest11@mail.ru"
towhome = "fromtest11@mail.ru"
mypass = "geekbrain00"
reportname = "log.txt"

msg = MIMEMultipart()
msg['From'] = fromwhome
msg['To'] = towhome
msg['Subject'] = "Привет от Garry"
text = "Avada kedavra"

msg.attach(MIMEText(text))

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = f'attachment; filename="{basename(reportname)}"'
    msg.attach(part)

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromwhome, mypass)
text = msg.as_string()
server.sendmail(fromwhome, towhome, text)
server.quit()
