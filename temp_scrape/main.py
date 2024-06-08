import selectorlib
import requests
import datetime as dt
import sqlite3

URL = "http://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data.db")

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text

    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['temp']
    return value

def store(extracted):
    date = dt.datetime.now().strftime('%y-%m-%d-%H-%M-%S')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?)", (date,extracted))
    connection.commit()

def main():
    s = scrape(URL)
    ex = extract(s)
    store(ex)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events;")
    row = cursor.fetchall()
    print(row)
    
if __name__ == '__main__':
    main()
