import socket


def index():
    return '<h1>Index Page</h1>'
    # with open('templates/index.html') as template:
    #     return template.read()


def blog():
    return '<h1>Blog Page</h1>'
    # with open('templates/blog.html') as template:
    #     return template.read()


URLS = {
    '/': index,
    '/blog': blog
}


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def generate_headers(method, url):
    if method != 'GET':
        return ('HTTP/1.1 405 Method not alllowed\n\n', 405)
    if url not in URLS:
        return ('HTTP/1.1 404 Not Found\n\n', 404)
    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return URLS[url]()


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()


def run():
    # AF_INET - IPv4
    # SOCK_STREAM - TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # SOL_SOCKET - указание на текущий сокет, SO_REUSEADDR, 1 - переиспользование порта
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # связывание субьекта(сервера) с адресом и портом
    server_socket.bind(('localhost', 5000))
    # указание серверу прослушивать адрес и порт на наличие входящих пакетов
    server_socket.listen()
    while True:
        # метод accept() возвращает кортеж
        client_socket, addr = server_socket.accept()
        # содержимое запроса клиента
        request = client_socket.recv(2048)
        print(request, addr)
        # request приходит от браузера в байтах, декодируем в текст
        response = generate_response(request.decode('utf-8'))
        client_socket.sendall(response)
        # всегда нужно закрывать сокет, чтобы увидеть что-то в браузере
        client_socket.close()


if __name__ == '__main__':
    run()
