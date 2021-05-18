from socket import *
import json

contentDiscovery = {}

serverPort = 5001

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind( ('', serverPort) )
print("The server is ready to receive")

while True:
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

# dic ={}

# a ={
#     "chunk":["wp_1","wp_2","wp_3","bl_1","bl_2","bl_3"]
# }
# b ={
#     "chunk":["wp_1","wp_2","wp_3","bl_1","bl_2","bl_3"]
# }

# for i in a["chunk"]:
#     if i not in dic:
#         dic[i]=[]

# for i in a["chunk"]:
#     if "1" not in dic[i]:
#         dic[i].append("1")
    
# for i in a["chunk"]:
#     if "1" not in dic[i]:
#         dic[i].append("1")

# print(dic)

# for i in a["chunk"]:
#     if i not in dic:
#         dic[i]=[]
        
# for i in a["chunk"]:
#     dic[i].append("2")
    
# print(dic)
