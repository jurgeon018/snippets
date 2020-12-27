import socket 
from select import select 


to_monitor = []

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost',5000))
    server_socket.listen()
    return server_socket



def accept_connection(server_socket):
    client_socket, address = server_socket.accept()
    to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        client_socket.send(f'Hello. Your request was: {request.decode()}'.encode())
    else:
        client_socket.close()
        to_monitor.remove(client_socket)

def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor,[],[])
        for socket in ready_to_read:
            if socket is server_socket:
                accept_connection(server_socket)
            else:
                send_message(socket)

if __name__ = '__main__':
    server_socket = server()
    to_monitor.append(server_socket)
    event_loop()




