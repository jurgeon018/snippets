import socket 


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost',8000))
server_socket.listen(1)


client_socket, address = server_socket.accept()
while True:
    request = client_socket.recv(1024)
    parsed_request = request.decode().split('\r\n')
    method = parsed_request[0]
    obj = {}
    for i in parsed_request[1:]:
        parsed_i = i.split(':', 1)
        key      = parsed_i[0]
        value    = parsed_i[-1]
        if key and value:
            obj[key] = value
    print(obj)
    if not request: break
    client_socket.send('henlo'.encode())
client_socket.close()

