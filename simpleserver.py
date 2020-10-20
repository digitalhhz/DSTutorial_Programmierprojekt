import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = '127.0.0.1'
server_port = 10001

# Buffer size
buffer_size = 1024

message = 'Hi client! Nice to connect with you!'

server_socket.bind((server_address, server_port))
print('Server up and running at {}:{}'.format(server_address, server_port))

while True:
    print('\nWaiting to receive message...\n')

    data, address = server_socket.recvfrom(buffer_size)
    print('Received message from client: ', address)
    print('Message: ', data.decode())

    if data:
        server_socket.sendto(str.encode(message), address)
        print('Replied to client: ', message)