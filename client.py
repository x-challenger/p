import socket
import sys


remote_addr, port = sys.argv[1:]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((remote_addr, port))


print("connection established.")

while True:

    input_ = input(f"{remote_addr}>")

    client_socket.sendall(input_.encode("utf-8"))
    data = client_socket.recv(-1)
    print(f"{len(data)} bytes received")
    print(f"response:{data.decode('utf-8')}")




