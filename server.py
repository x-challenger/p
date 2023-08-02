import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(socket.gethostname(), 80)

server_socket.listen(6)

while True:
    client_socket, address = server_socket.accept()

    while True:

        data = client_socket.recv(1024)
        if not data:
            continue



        print(f"{len(data)} bytes received")
        print(f"data:{data.decode('utf-8')}")

        response = "data received -- response from server".encode("utf-8")
        client_socket.send(response)
        if data == "exit".encode("utf-8"):
            client_socket.send("connection will be closed.")
            break
    
    client_socket.close()

    
