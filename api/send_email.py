import smtplib, ssl

def send_email(msg):
    host = "smtp.gmail.com"
    port = 465
    username = "rutyreal@gmail.com"
    password = "vmcf tcvr mtmy eqwc"
    reciever = "rutyreal@gmail.com"
    context = ssl.create_default_context()
    message = msg
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

