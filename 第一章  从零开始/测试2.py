import socket
import os
import subprocess

host = 'x.200.x.30'
port = 12345

obj = socket.socket()
obj.connect((host, port))
cmd = 'netstat -ano | findstr %s' % port
result1 = subprocess.getoutput(cmd)
print(result1)
i = 0
while True:
    obj.send(bytes("This is %s msg from client" % i, encoding="utf-8"))
    i = i + 1
    print(i)
    if i == 5:
        obj.send(bytes("End", encoding="utf-8"))
        ret = str(obj.recv(1024), encoding="utf-8")
        print(ret)
        if ret == 'Finish!':
            # obj.close()
            break
    else:
        continue
result2 = subprocess.getoutput(cmd)
print(result2)
