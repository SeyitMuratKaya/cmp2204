from socket import *
import json

clientSocket = socket(AF_INET, SOCK_STREAM)

requestedFile = input("Which file you want to download ?")

contentFile =  open('contents.txt','r')

lookupJson = contentFile.read()
contentFile.close()

lookupDictionary = json.loads(lookupJson)

for i in range(1,6):
    chunk = requestedFile + '_' + str(i)
    if chunk in lookupDictionary:
        # print(lookupDictionary[chunk][0])
        serverName = lookupDictionary[chunk][0]
        serverPort = 8000
        clientSocket.connect((serverName,serverPort))
        request = {
            "requested_content": chunk
        }
        requestJson = json.dumps(request)
        clientSocket.send(requestJson.encode('utf-8'))
    else:
        print('chunk '+ chunk + ' does not exist')
        
    clientSocket.close()

