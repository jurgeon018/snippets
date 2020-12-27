import socket 


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost',5000))
    server_socket.listen()
    return server_socket


# 1
def func1():
    server_socket = server()

    while True:
        client_socket, address = server_socket.accept()
        while True:
            request = client_socket.recv(4096)
            if not request: break
            client_socket.send(f'Hello. Your request was: {request.decode()}'.encode())
        client_socket.close()

# 2
def func2():
    server_socket = server()

    def accept_connection(server_socket):
        while True:
            client_socket, address = server_socket.accept()
            send_message(client_socket)

    def send_message(client_socket):
        while True:
            request = client_socket.recv(4096)
            if not request: break
            client_socket.send(f'Hello. Your request was: {request.decode()}'.encode())
        client_socket.close()

    accept_connection(server_socket)

if __name__ == '__main__':
    func1()
    # # or
    # func2()


