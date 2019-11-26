import socket
import sys
import threading
import time


def server():
    def bind():

        HOST = '127.0.0.1'

        s.bind((HOST, 8855))

        print("bind ok")

    def listen():

        s.listen(10)

        print('Socket now listening')

    def send_sth(conn):

        while True:

            try:

                sth = input('say something:\n')

                conn.sendall(sth.encode('utf-8'))

            except ConnectionError:

                print('connect error')

                sys.exit(-1)

            except:

                print('unexpect error')

                sys.exit(-1)

    def recv(conn):

        while True:

            try:

                data = conn.recv(1024)

                data2 = data.decode('utf-8')

                print('get message:' + data2)

            except ConnectionError:

                print('connect error')

                sys.exit(-1)

            except:

                print('unexpect error')

                sys.exit(-1)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    bind()

    listen()

    conn, addr = s.accept()

    print("connect success")

    print('connect time: ' + time.ctime())

    threading._start_new_thread(recv, (conn,))

    send_sth(conn)


if __name__ == '__main__':
    server()
