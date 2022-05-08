import os
import socket
from udp_server import UDPServer
from udp_server_log import UDPServerLog
from repository import Repository

if __name__ == '__main__':

    server_ip = os.getenv("SERVER_IP") or "127.0.0.1"
    server_port = os.getenv("SERVER_PORT") or 20000
    buffer_size = os.getenv("BUFFER_SIZE") or 100000000

    repository = Repository()

    udp_server_log = UDPServerLog()
    udp_server = UDPServer(server_ip, server_port, buffer_size, repository, udp_server_log)
    udp_server.open_socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.receive_packets()