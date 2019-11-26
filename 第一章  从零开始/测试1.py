import socket
import os
import time


def main():
    while True:
        ret = str(conn.recv(1024), encoding="utf-8")
        print(ret)
        if 'End' in ret:
            print('End')
            conn.sendall(bytes("Finish!", encoding="utf-8"))
            # conn.close()#sk.close 不发送fin包
            os.system('netstat -ano | findstr %s' % port)
            break
        else:
            print('Not close')
            continue


if __name__ == '__main__':
    while True:
        host = 2500
        port = 12345
        sk = socket.socket()
        sk.bind((host, port))
        sk.listen(5)
        # sk.settimeout(10)
        print('The port is listening...')
        os.system('netstat -ano | findstr %s' % port)
        print('Wait for the client.')
        conn, address = sk.accept()
        print('Connecting...')
        print('Connect from: ', address)
        os.system('netstat -ano | findstr %s' % port)
        main()
