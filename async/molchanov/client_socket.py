import socket 
import argparse 
# https://habr.com/ru/post/144416/
parser = argparse.ArgumentParser(description='hello')
parser.add_argument(
    '-hs', 
    '--host',
    action='store', 
    dest='host', 
    help='host',
    type=str,
    default='localhost',
)
parser.add_argument(
    '-p', 
    '--port',
    action='store', 
    dest='port', 
    help='port',
    type=int,
    default=5000,
)
parser.add_argument(
    '-m', 
    '--message',
    action='store', 
    dest='message', 
    help='message',
    type=str,
    default='hello!',
)
args  = parser.parse_args()

client_socket = socket.socket()
client_socket.connect((args.host, args.port))
request  = client_socket.send(args.message.encode())
response = client_socket.recv(4096) 
print(f'response: {response.decode()}')
client_socket.close()
