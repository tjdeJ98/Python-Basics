from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


message = MIMEMultipart()
message["from"] = "Timo de Jong"
message["to"] = "timobigtv@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@timo.com", "woopwoop")
    smtp.send_message(message)
    print("Sent...")
