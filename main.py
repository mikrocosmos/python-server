import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 1333))
server.listen(4)
print('Waiting...')
clientSocket, address = server.accept()
data = clientSocket.recv(1024).decode('utf-8')
print(data)
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
content = 'Well done.'.encode('utf-8')
clientSocket.send(HDRS.encode('utf-8') + content)
print('No trains are currently in service')