import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

bcname = "<HOST>"
bcmessage = input("Broadcast message: ")

print("Server is running, waiting for connection...")

bind_ip = local_ip
bind_port = 13351

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((bind_ip, bind_port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been triggered!")
    clientsocket.send(bytes(bcname+bcmessage, "utf-8"))
    clientsocket.close()