import socket

bind_ip = input("Host IP: ")
bind_port = 13351

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((bind_ip, bind_port))

full_msg = ''
while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)