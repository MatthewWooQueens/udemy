import selectorlib
import requests
import streamlit as st
import plotly.express as px
import datetime as dt

URL = "http://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

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
    with open("data.txt", "a") as file:
        file.write(f'{date},{extracted}\n')

def main():
    s = scrape(URL)
    ex = extract(s)
    store(ex)

if __name__ == '__main__':
    main()
