import os
import socket

class UDPClientLog:

    def log_socket(self):
        print(f"UDP client socket created successfully")

    def log_server_response(self, message):
        print(f"UDP client received the next message from server: {message}")