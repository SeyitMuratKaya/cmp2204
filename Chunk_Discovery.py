from socket import *
import json

contentDiscovery = {

}

serverPort = 5001


serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind( ('', serverPort) )
print("The server is ready to receive")

while True:
    message, (clientAddress,clientPort) = serverSocket.recvfrom(2048)
    print('received {} bytes from {}'.format(len(message), clientAddress))
    x = json.loads(message)
    for i in x['chunk']:
        contentDiscovery[i] = [clientAddress]
    print(contentDiscovery)
