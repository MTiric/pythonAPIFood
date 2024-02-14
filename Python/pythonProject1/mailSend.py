import smtplib
import ssl
from email.message import EmailMessage


def sendMail(mail_recipient, token):
    email_sender = 'jenkinsmtiric@gmail.com'
    email_password = 'hoxaomqupdadaswv'
    email_receiver = mail_recipient

    subject = 'User account confirmation - VitaMe'
    body = f"""
    Please press the link below to confirm your mail:
    http://192.168.1.7:5000/register{token}
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    print("Poslan mail za potvrdu maila")
