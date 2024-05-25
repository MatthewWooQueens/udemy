import requests

api_key = "a017f7d89ba24a81a42d155702ef08c6"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-04-25&sortBy=publishedAt&apiKey=a017f7d89ba24a81a42d155702ef08c6"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
