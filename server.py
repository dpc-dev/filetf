#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import string,os,threading,time,sys
from socket import *


def tou(ss,addr):
    print('有人上钩了........',addr)
    n = ss.recv(1024)
    ss.send('ok'.encode())
    time.sleep(1)
    
    print(int(n.decode()))
    
    for i in range(int(n.decode())):
        
        filename = ss.recv(1024)
        
        
    
        print(filename)   
        f = open(filename.decode(),'wb')
        ss.send('ok'.encode())
        while True:
            data = ss.recv(2048)
            if  data== 'ok'.encode():
                
                print('传输完成.......')
                break
            f.write(data)
        f.close()
    ss.close()




os.chdir(sys.path[0])
with open('server.txt','r') as  f:
    data =  f.read()

try:
    adc = ('127.0.0.1',int(data))
except ValueError:
    print('配置文件写入错误......')
    sys.exit(1)
sock = socket(AF_INET,SOCK_STREAM)
try:
    sock.bind(adc)
except TypeError:
    print('配置文件错误...')
sock.listen(5)
while True:
    print('等待中.....')
    ss,addr=sock.accept()
    t = threading.Thread(target=tou,args=(ss,addr))
    t.start()