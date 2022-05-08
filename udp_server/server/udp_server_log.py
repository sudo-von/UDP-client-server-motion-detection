import os
import socket

class UDPServerLog:

    def log_socket(self, local_ip, port):
        print(f"UDP server at: {local_ip}:{port}")

    def log_client(self, message, address):
        client_message = "Message from Client:{}".format(message)
        client_ip  = "Client IP Address:{}".format(address)
        print(client_message)
        print(client_ip)