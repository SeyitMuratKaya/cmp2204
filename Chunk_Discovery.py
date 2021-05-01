from socket import *
import json

contents = {

}

serverPort = 5001


serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind( ('', serverPort) )
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('received {} bytes from {}'.format(len(message), clientAddress))
    x = json.loads(message)
    print(clientAddress)