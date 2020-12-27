import requests
import re
import json
# 1.Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.


def write_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)


def read_file_data(filename):
    with open(filename, 'r') as f:
        print(f.read())
        # for line in f:
        #     print(line)


# write_to_file('hahaha.txt', 'This is the line of text.\nAnother.\nLast')
# read_file_data('hahaha.txt')

# 2.Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/comments, выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

def print_headers_and_save_json(filename):
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    headers = dict(r.headers)
    for k, v in headers.items():
        print(f'{k}:{v}')
    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size=128):
            file.write(chunk)


def print_headers_and_save_json2(filename):
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    json_dict = {}
    for header, value in r.headers.items():
        json_dict[header] = value
        print(f'{header}:{value}')
    with open(filename, 'w') as f:
        json.dumps(json_dict, sort_keys=True, indent=4)


print_headers_and_save_json('jsonplaceholdercomments.json')
print_headers_and_save_json2('site_response.json')

# 3.Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
# Ответить себе на вопрос удобно ли так делать?


def extract_links(url):
    r = requests.get(url)
    pattern = r'href="(.*?)"'
    links = re.findall(pattern, r.text, flags=re.IGNORECASE)
    with open('site_links1.txt', 'a') as f:
        for link in links:
            f.write(link)
    return links


def extract_links2(url):
    r = requests.get(url)
    pattern = r'<a[^><]*href=[\'"]([^><\'"]*)[\'"][^><]*>'
    links = re.findall(pattern, r.text)
    with open('site_links2.txt', 'a') as f:
        for link in links:
            f.write(link)
    return links


# print(extract_links('https://habrahabr.ru/'))
# print(extract_links('http://www.moscowpython.ru/meetup/46/'))
# print(extract_links2('https://habrahabr.ru/'))
# print(extract_links2('http://www.moscowpython.ru/meetup/46/'))


#  PRACTICE

# [22/Jun/2017 13:53:22] DEBUG [django.db.backends.schema:103] CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
# [22/Jun/2017 13:53:22] DEBUG [django.db.backends:90] (0.022) CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); args=None
# [22/Jun/2017 13:53:22] DEBUG [django.db.backends.schema:103] ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params [])
# [22/Jun/2017 13:53:22] DEBUG [django.db.backends:90] (0.001) ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_76bd3d3b_uniq" UNIQUE ("app_label", "model"); args=[]

# Дан текстовый файл(лог), нужно при помощи регулярных выражений вытащить из него дату, url и код ответа. Посчитать сколько чего было, вывести сумму в консоль
#
# При помощи библиотеки requests нужно скачать содерживое страниц reddit.com/r/python (любой тред > 5 комментариев) и в консоль вывести пару: автор комментария и его текст
#
# Дана ссылка на пользовтеля habrahabr, нужно при помощи scrappy скачать всего его статьи и сохранить их в json файл
