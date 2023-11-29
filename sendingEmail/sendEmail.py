import smtplib
import ssl          # secure socket layer
from email.message import EmailMessage

subject = "Email from Python. "
body = "This is a test email from Python!"

sender_email= "senderName.surname@gmail.com"
receiver_email="receiverName.surname@gmail.com"

password=input("Enter a password: ")

message = EmailMessage()
message["From "] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")

context = ssl.create_default_context()      # secure connection


print("Sending Email")
# connecting with ssl
# connecting gmail, port for connection,
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")