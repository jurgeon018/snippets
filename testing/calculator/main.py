import requests
import time 


class Calculator:
    def add(self, a, b):
        # long running process
        time.sleep(10)
        return a + b


class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)
