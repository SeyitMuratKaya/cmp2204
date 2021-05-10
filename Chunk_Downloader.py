from socket import *
import json

serverName = 'localhost'
serverPort = 8000

requestedFile = input("Enter file name ")

contentFile = open("contents.txt",'r')

lookupJson = contentFile.read()
contentFile.close()

lookupDictionary = json.loads(lookupJson)

for i in range(1,6):

    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverName,serverPort))
    
    print(i)
    chunk = requestedFile + '_' + str(i) 

    request = {
        "requested_content": chunk
    }
    requestJson = json.dumps(request)

    clientSocket.send(requestJson.encode())
    print("request sended")

    with open('./rec/file'+"_"+str(i), "wb") as f:
        while True:
            bytes_read = clientSocket.recv(4096)
            print(len(bytes_read))
            if len(bytes_read) <= 0:
                break
            f.write(bytes_read)
    print("file received")

    clientSocket.close()


