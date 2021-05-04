from socket import *
import json

serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

print('The server is ready to receive')

connection , addr = serverSocket.accept()


print("waiting for request")
requestJson =  connection.recv(4096).decode()
print("requiest received")

requestedFile = json.loads(requestJson)


filename = requestedFile['requested_content']

with open(filename,'rb') as file:
    while True:
        bytes_read = file.read(4096)
        if not bytes_read:
            break
        connection.sendall(bytes_read)


print("file sended")

        




