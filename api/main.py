import requests
from send_email import send_email

api_key = "a017f7d89ba24a81a42d155702ef08c6"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-04-25&sortBy=publishedAt&apiKey=a017f7d89ba24a81a42d155702ef08c6"

request = requests.get(url)
content = request.json()
msg = "Subject: Today's News\n"
for article in content["articles"]:
    msg = ''.join((msg, f'{article["title"]}\n{article["description"]}\n\n',))
#msg = u''.join(msg).encode('utf-8').strip()
msg = msg.encode('utf-8')
send_email(msg)
