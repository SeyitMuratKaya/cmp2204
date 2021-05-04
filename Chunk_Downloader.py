from socket import *
import json

serverName = 'localhost'
serverPort = 8000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

requestedFile = input("Enter file name ")

contentFile = open("contents.txt",'r')

lookupJson = contentFile.read()
contentFile.close()

lookupDictionary = json.loads(lookupJson)


chunk = requestedFile + '_' + str(1) 

request = {
    "requested_content": chunk
}
requestJson = json.dumps(request)

clientSocket.send(requestJson.encode())
print("request sended")

with open('./rec/file'+str(1), "wb") as f:
    while True:
        bytes_read = clientSocket.recv(4096)
        print(len(bytes_read))
        if not bytes_read:
            break
        f.write(bytes_read)
print("file received")


