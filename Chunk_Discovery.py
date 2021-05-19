from socket import *
import json

contentDiscovery = {}

serverPort = 5001

print("Server is ready to receive")

while True:
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    serverSocket.bind( ('', serverPort) )

    message, (clientAddress,clientPort) = serverSocket.recvfrom(2048)
    print('Received {} bytes from {}'.format(len(message), clientAddress))
    receivedChunks = json.loads(message)

    for i in receivedChunks['chunk']:
        if i not in contentDiscovery:
            contentDiscovery[i] = []

    for i in receivedChunks['chunk']:
        if clientAddress not in contentDiscovery[i]:
            contentDiscovery[i].append(clientAddress)

    contentFile = open("contents.txt", "w")
    cfJson = json.dumps(contentDiscovery)
    contentFile.write(cfJson)
    contentFile.close()

    print("Available chunks are:",'\n',contentDiscovery)