import cv2

class MotionDetection:
    def __init__(self, log_service):
        self.log_service = log_service
        self.camera = None 
        self.static_back = None

    def open_camera(self, camera_number):
        self.camera = cv2.VideoCapture(camera_number)
        if not self.camera.isOpened():
            self.log_service.log_camera_error(camera_number)
            exit()
        self.log_service.log_camera()

    def handle_motion(self):
        while True:
            motion = 0
            check, frame = self.camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            if self.static_back is None:
                self.static_back = gray
                continue

            diff_frame = cv2.absdiff(self.static_back, gray)
            thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
        
            cnts,_ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in cnts:
                if cv2.contourArea(contour) < 10000:
                    continue
                motion = 1
                return self.get_frame_bytes(frame)
        

    def get_frame_bytes(self, frame):
        scale_percent = 50
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dsize = (width, height)
        output = cv2.resize(frame, dsize)
        return cv2.imencode('.jpg', output)[1].tobytes()