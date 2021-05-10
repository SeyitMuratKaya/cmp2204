from socket import *
import json
from datetime import datetime

serverName = 'localhost'
serverPort = 8000

requestedFile = input("Enter file name ")

contentFile = open("contents.txt",'r')

lookupJson = contentFile.read()
contentFile.close()

lookupDictionary = json.loads(lookupJson)

for i in range(1,6):

    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect(("192.168.1.24",serverPort))
    
    print(i)
    chunk = requestedFile + '_' + str(i) 

    request = {
        "requested_content": chunk
    }
    requestJson = json.dumps(request)

    clientSocket.send(requestJson.encode())
    print("request sended")

    with open('file'+"_"+str(i), "wb") as f:
        while True:
            bytes_read = clientSocket.recv(4096)
            print(len(bytes_read))
            if len(bytes_read) <= 0:
                break
            f.write(bytes_read)
    print("file received")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    uploader_ip = 122321312 

    with open("download_log.txt","a") as file:
        file.write(f"chunk {chunk} downloaded from {uploader_ip} at {current_time} \n")



    clientSocket.close()



content_name = requestedFile  # again, this'll be the name of the content that used wanted to download from the network.
chunknames = [content_name+'_1', content_name+'_2', content_name+'_3', content_name+'_4', content_name+'_5']
  
#with open(content_name+'.png', 'w') as outfile: 
with open('hello.png', 'wb') as outfile: # in your code change 'ece.png' to content_name+'.png'
    for chunk in chunknames: 
        with open(chunk, 'rb') as infile: 
            outfile.write(infile.read() )
        infile.close() 




