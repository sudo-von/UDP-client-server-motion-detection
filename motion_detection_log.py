import os
import socket

class MotionDetectionLog:

    def log_camera(self):
        print(f"Camera open successfully")

    def log_camera_error(self, camera_number):
        print(f"Error: Can't open camera {camera_number}")