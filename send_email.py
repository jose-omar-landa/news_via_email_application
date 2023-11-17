import smtplib, ssl

# function to send an email via python
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # add your email address for username, and create an app password on your gmail account for the password variable
    username = "EMAIL_HERE"
    password = "APP_PASSWORD_HERE"

    # add the recipient email for the receiver variable
    receiver = "RECEIVER_EMAIL_HERE"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
