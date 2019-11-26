import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8000))
sock.listen()

while True:
    conn, addr = sock.accept()
    data = conn.recv(8096)
    # 给回复的消息加上响应状态行
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"OK")
    conn.close()
