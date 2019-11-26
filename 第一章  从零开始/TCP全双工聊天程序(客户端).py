import socket
import sys
import threading
import time
class client():

    def __init__(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ip = "127.0.0.1"



    def connect(self):

        try:

            self.s.connect((self.ip, 8855))

            print("connect success")

            print('connect time: ' + time.ctime())

        except ConnectionError:

            print('connect error')

            sys.exit(-1)

        except:

            print('unexpect error')

            sys.exit(-1)



    def send_sth(self):

        while True:

            sth = input('say something:\n')

            try:

                self.s.sendall(sth.encode('utf-8'))

            except ConnectionError:

                print('connect error')

                sys.exit(-1)

            except:

                print('unexpect error')

                sys.exit(-1)



    def receive(self):

        while True:

            try:

                r = self.s.recv(1024)

                print('get message:' + r.decode('utf-8'))

            except ConnectionError:

                print('connect error')

                sys.exit(-1)

            except:

                print('unexpect error')

                sys.exit(-1)





c1 = client()

c1.connect()

threading._start_new_thread(c1.receive, ())

c1.send_sth()