from bs4 import BeautifulSoup
import requests
import csv
from peewee import *

db = SqliteDatabase('app.db')

class Article(Model):
    class Meta:
        database = db
    header = CharField()
    date = CharField()
    content = TextField()
    link = TextField()

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('bs_corey.csv', 'a') as f:
        order = ['header','date','content','link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def write_db():
    db.connect()
    db.create_tables([Article])
    with open('bs_corey.csv', 'r') as f:
        order = ['header','date','content','link']
        reader = csv.DictReader(f, fieldnames=order)
        articles = list(reader)
        with db.atomic():
            for article in articles:
                Article.create(**article)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    for article in soup.find_all('article'):
        try:
            header = article.find('a', class_='entry-title-link').text
        except:
            header = ''
        try:
            date = article.find('time', class_='entry-time').text
        except:
            date = ''
        try:
            content = article.find('div', class_='entry-content').find('p').text
        except:
            content = ''
        try:
            link = 'https://youtube.com/watch?v='+article.find('div', class_='entry-content').find('iframe', class_='youtube-player').get('src').split('?')[0].split('/')[-1]
            # vid_id = article.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
        except:
            link = ''
        data = {'header':header, 'date':date, 'content':content, 'link':link}
        write_csv(data)

def main():
    for x in range(1, 17):
        url = f'https://coreyms.com/page/{x}'
        get_data(get_html(url))
    write_db()

if __name__ == '__main__':
    main()
