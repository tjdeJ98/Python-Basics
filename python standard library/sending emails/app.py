from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


message = MIMEMultipart()
message["from"] = "Timo de Jong"
message["to"] = "timobigtv@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
