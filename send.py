import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'lexa324sa@gmail.com'
msg['To'] = 'shargatov99@mail.ru'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('lexa324sa@gmail.com', '6ZKpNki8')

mailserver.sendmail('lexa324sa@gmail.com','shargatov99@mail.ru',msg.as_string())

mailserver.quit()