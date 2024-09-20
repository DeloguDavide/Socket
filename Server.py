import socket


server_address = ("192.168.65.19", 6980)#2 dati in una tupla, ip e porta
BUFFER_SIZE = 4092 #quando ricevo dei dati dichiaro quanti bit usare, se mando qualcosa di più grande avvengono troncamenti
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(server_address)
data, address = udp_server_socket.recvfrom(BUFFER_SIZE)#Metto in ascolto, sono bloccato/programma si ferma
print(f"Messaggio ricevuto: {data.decode} da {address}")#decode per convertire
