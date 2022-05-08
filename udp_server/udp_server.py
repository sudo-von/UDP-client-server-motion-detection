import os
import socket

class UDPServer:

    def __init__(self, local_ip, local_port, buffer_size, repository, log_server):
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size
        self.repository = repository
        self.log_server = log_server
        self.socket = None 

    def open_socket(self, socket_family, socket_type):
        self.socket = socket.socket(family=socket_family, type=socket_type)
        self.socket.bind((self.local_ip, self.local_port))
        self.log_server.log_socket(self.local_ip, self.local_port)

    def receive_packets(self):
        while(True):
            bytes_address_pair = self.socket.recvfrom(self.buffer_size)
            message, address = bytes_address_pair
            self.log_server.log_client(message, address)
            self.send_packets(str.encode("Bytes received successfuly"), address)
            self.repository.store(message)

    def send_packets(self, bytes_to_send, address):
        self.socket.sendto(bytes_to_send, address)