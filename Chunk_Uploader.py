from socket import *
import json

serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

print('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    requestJson = connectionSocket.recv(1024)
    request = json.loads(requestJson)

    openFile = open(request["requested_content"],'r')
    requestedChunk = openFile.read()
    
    while (requestedChunk):
        connectionSocket.send(requestedChunk)
        requestedChunk = openFile.read(1024)
    connectionSocket.close()
    
    
    print(requestedChunk)
    # connectionSocket.send(requestedChunk.encode('utf-8'))
    # connectionSocket.close()