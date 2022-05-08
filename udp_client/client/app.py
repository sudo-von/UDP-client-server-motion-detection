import os
import socket
from udp_client import UDPClient
from udp_client_log import UDPClientLog
from motion_detection import MotionDetection
from motion_detection_log import MotionDetectionLog
from service import Service
from service_log import ServiceLog

if __name__ == '__main__':

    server_ip = os.getenv("SERVER_IP") or "127.0.0.1"
    server_port = int(os.getenv("SERVER_PORT")) or 20000
    buffer_size = int(os.getenv("BUFFER_SIZE")) or 100000000

    udp_client_log = UDPClientLog()
    udp_client = UDPClient(server_ip, server_port, buffer_size, udp_client_log)
    udp_client.open_socket(socket.AF_INET, socket.SOCK_DGRAM)

    motion_detection_log = MotionDetectionLog()
    motion_detection = MotionDetection(motion_detection_log)
    motion_detection.open_camera(0)

    service_log = ServiceLog()
    service = Service(udp_client, motion_detection, service_log, 5)
    service.start()