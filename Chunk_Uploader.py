from socket import *
import json

serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

print('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    print("connected")

    requestJson = connectionSocket.recv(1024)
    request = json.loads(requestJson)

    openFile = open(request["requested_content"],'rb')
    print(request["requested_content"])
    requestedChunk = openFile.read(1024)
    
    while (requestedChunk):
        connectionSocket.send(requestedChunk)
        print("file sended")
        requestedChunk = openFile.read(1024)
    openfile.close()


    print("file sended")
    connectionSocket.close()
    
    # print(requestedChunk)
    # connectionSocket.send(requestedChunk.encode('utf-8'))
    # connectionSocket.close()