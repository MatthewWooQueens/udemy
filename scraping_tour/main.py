import requests
import selectorlib
import smtplib
import ssl

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

'''Scrape the page source from the URL'''
def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text

    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "rutyreal@gmail.com"
    password = "vmcf tcvr mtmy eqwc"

    reciever = "rutyreal@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username,password)
        server.sendmail(username, reciever, message)

def store(extracted):
    with open("data.txt", "w") as file:
        file.write(extracted + '\n')

def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email(message="Hey, New event was found!")
