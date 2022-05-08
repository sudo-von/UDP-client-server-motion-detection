import time

class Service:
    def __init__(self, udp_client, motion_detection, log_service, interval):
        self.udp_client = udp_client
        self.motion_detection = motion_detection
        self.log_service = log_service
        self.interval = interval

    def start(self):
        self.log_service.start()
        bytes_to_send = self.motion_detection.handle_motion()
        while bytes_to_send:
            bytes_to_send = self.motion_detection.handle_motion()
            self.udp_client.send_packets(bytes_to_send)
            time.sleep(self.interval)
