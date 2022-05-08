import cv2


class MotionDetection:
    def __init__(self, log_service):
        self.log_service = log_service
        self.camera = None 

    def open_camera(self, camera_number):
        self.camera = cv2.VideoCapture(camera_number)
        if not self.camera.isOpened():
            self.log_service.log_camera_error(camera_number)
            exit()
        self.log_service.log_camera()

    def detect_movement(self):
        static_back = None
        while True:
            motion = 0
            check, frame = self.camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            if static_back is None:
                static_back = gray
                continue

            diff_frame = cv2.absdiff(static_back, gray)
            thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
        
            cnts,_ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in cnts:
                if cv2.contourArea(contour) < 10000:
                    continue
                motion = 1
        
            self.draw_rectangle(frame, contour)
            self.show_frames(gray, diff_frame, thresh_frame, frame)
            self.handle_exit(cv2.waitKey(1))

    def show_frames(self, gray, diff_frame, thresh_frame, frame):
        cv2.imshow("Gray frame", gray)
        cv2.imshow("Difference frame", diff_frame)
        cv2.imshow("Threshold frame", thresh_frame)
        cv2.imshow("Color frame", frame)

    def draw_rectangle(self, frame, contour):
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        print(len(image_bytes))
        print("movimiento detectado eprro")

    def handle_exit(self, key):
        if key == ord('q'):
            self.camera.release()
            exit()