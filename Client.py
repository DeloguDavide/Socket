
import socket as s

udp_client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

message = "ciao".encode('utf8')

server_address = ("192.168.65.103", 6980)
BUFFER_SIZE = 4092 #uanti bit posso inviare o ricevere

udp_client_socket.sendto(message, server_address)

# import socket as s

# client = s.socket(s.AF_INET, s.SOCK_STREAM)

# host = '192.168.65.103'
# port = 22222

# client.connect((host, port))

# client.send("ciao dall'host n".encode('utf-8'))
# print(client.recv(1024).decode('utf-8'))
# client.close()