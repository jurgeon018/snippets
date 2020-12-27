import requests
##################################################
# CoreyMs
r = requests.get('https://imgs.xkcd.com/comics/python.png')
(r.headers)
with open('./comic.png', 'wb') as f:
    f.write(r.content)

r = requests.get('http://httpbin.org/get', params={'page':2, 'count':25})
(r.text)
(r.url)

r = requests.get('http://httpbin.org/basic-auth/jurgeon018/yfpfhrj69018', auth=('jurgeon018', 'yfpfhrj69018'))
(r.text)
r = requests.get('http://httpbin.org/delay/6', timeout=3)
print(r)

r = requests.post('http://httpbin.org/post', data={'username':'corey', 'password':'yfpfhrj69'})
(r.text)
(r.json()['form'])



##################################################
# Official DOcumentation

# ==== requests.get()
r = requests.get('https://api.github.com/events', params={'key1': 'value1', 'key2': 'value2'})

r = requests.get('https://api.github.com/some/endpoint', headers={'user-agent': 'my-app/0.0.1'})

r = requests.get('https://api.github.com/events', params={'key1': 'value1', 'key2': 'value2'})
r.json()
r.url
r.text
r.content
r.encoding
r.status_code
r.raise_for_status
r.headers
r.iter_content()

r = requests.get('https://api.github.com/events', stream=True)
r.raw.read(10)
# with open('/home/jurgeon/filename.txt', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=10):
#         fd.write(chunk)

# ==== requests.post() ====
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
r = requests.post('https://api.github.com/some/endpoint', json={'some': 'data'})
# ==== requests.put() ====
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# ==== requests.delete() ====
r = requests.delete('https://httpbin.org/delete')
# ==== requests.head() ====
r = requests.head('https://httpbin.org/get')
# ==== requests.options() ====
r = requests.options('https://httpbin.org/get')
