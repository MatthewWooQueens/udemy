import smtplib, ssl

def send_email(msg):
    host = "smtp.gmail.com"
    port = 465
    username = "johndoe@gmail.com"
    password = "b,oammdsa"
    reciever = "johndoe@gmail.com"
    context = ssl.create_default_context()
    message = "you suck"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
