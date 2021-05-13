import os
import math
import socket
import time
import json
import glob

serverPort = 5001

content_name = input('Enter file name:')  # This'll be the parameter you provide for this code. The name of the content that the user wants to download.
filename = content_name+'.png'
c = os.path.getsize(filename)
#print(c)
CHUNK_SIZE = math.ceil(math.ceil(c)/5) 
#print(CHUNK_SIZE)

index = 1
with open(filename, 'rb') as infile:
    chunk = infile.read(int(CHUNK_SIZE))
    while chunk:
        chunkname = content_name+'_'+str(index)
        #print("chunk name is: " + chunkname + "\n")
        with open(chunkname,'wb+') as chunk_file:
            chunk_file.write(chunk)
        index += 1
        chunk = infile.read(int(CHUNK_SIZE))
chunk_file.close()

print("Content seperated to 5 chunks")

files = {
    "chunk":[]
}
path = content_name + '_' + '[1-5]'
chunks = glob.glob(path)

for i in chunks:
    files["chunk"].append(i)

filesJson = json.dumps(files)
# print(files["chunk"])
print(filesJson)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# server.settimeout(0.2)

# message = b"your very important message"

while True:
    server.sendto(filesJson.encode('utf-8'), ('255.255.255.255', serverPort))
    print("message sent!")
    time.sleep(10)

