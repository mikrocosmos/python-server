import socket

def serverStart():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 1333))
        server.listen(4)
        while True:
            print('Waiting...')
            clientSocket, address = server.accept()
            data = clientSocket.recv(1024).decode('utf-8')
            # print(data)
            content = loadPage__get(data)
            clientSocket.send(content)
            clientSocket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Shutdown')

def loadPage__get(requestData):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = requestData.split(' ')[1]
    response = ''
    try:
        with open('dist'+path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + "Page not found :/").encode('utf-8')


if __name__ == '__main__':
    serverStart()