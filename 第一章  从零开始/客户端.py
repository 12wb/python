import socket

client = socket.socket()
client.connect(('127.0.0.1',1523))
while 1:
    # client.send(b'byebye')
    msg = client.recv(1024).decode().lower()
    print(msg)
    if msg == 'q': break
    send_msg = input('msg:').lower().strip()
    client.send(send_msg.encode())
    if send_msg == 'q': break


client.close()