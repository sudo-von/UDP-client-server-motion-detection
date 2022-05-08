import os
import socket
from udp_server import UDPServer
from udp_server_log import UDPServerLog
from udp_client import UDPClient
from udp_client_log import UDPClientLog
from motion_detection import MotionDetection
from motion_detection_log import MotionDetectionLog

if __name__ == '__main__':

    bytes_to_send = str.encode('VoN')

    server_ip = os.getenv("SERVER_IP") or "127.0.0.1"
    server_port = os.getenv("SERVER_PORT") or 20000
    buffer_size = os.getenv("BUFFER_SIZE") or 1024

    udp_server_log = UDPServerLog()
    udp_server = UDPServer(server_ip, server_port, buffer_size, udp_server_log)
    udp_server.open_socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.receive_packets()

    udp_client_log = UDPClientLog()
    udp_client = UDPClient(server_ip, server_port, buffer_size, udp_client_log)
    udp_client.open_socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.send_packets(bytes_to_send)

    motion_detection_log = MotionDetectionLog()
    motion_detection = MotionDetection(motion_detection_log)
    motion_detection.open_camera(2)
    motion_detection.detect_movement()