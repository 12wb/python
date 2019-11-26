import socket

server = socket.socket()
server.bind(('127.0.0.1',1523))
server.listen(5)

flag = 1
while flag:
    conn, addr = server.accept()

    while 1:
        send_msg = input('msg:').strip().lower()
        conn.send(send_msg.encode())
        if send_msg == 'q':
            flag = 0
            break
        msg = conn.recv(1024).decode()
        if msg == 'q': break
        print(msg)
    print('当前客户端断开连接等待新的连接')
    cmd = input('输入(q)退出，其他返回聊天:').strip().lower()
    if cmd == 'q':
        flag = 0
    conn.close()

server.close()