import socket

class UDPClient:

    def __init__(self, server_ip, server_port, buffer_size, log_service):
        self.server_ip = server_ip
        self.server_port = server_port
        self.buffer_size = buffer_size
        self.log_service = log_service
        self.socket = None 

    def open_socket(self, socket_family, socket_type):
        self.socket = socket.socket(family=socket_family, type=socket_type)
        self.log_service.log_socket()

    def receive_packets(self):
        message_from_server = self.socket.recvfrom(int(self.buffer_size)*2)
        self.log_service.log_server_response(message_from_server[0])

    def send_packets(self, bytes_to_send):
        self.socket.sendto(bytes_to_send, (self.server_ip, self.server_port))
        self.receive_packets()