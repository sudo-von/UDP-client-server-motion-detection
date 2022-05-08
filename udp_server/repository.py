import time
import os
from datetime import datetime

class Repository:

    def store(self, data):
        date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S").split(' ')
        date, time = date_time

        dirPath = f"{os.getcwd()}/images/{date}"
        dirExist = os.path.exists(dirPath)
        if not dirExist:
            os.makedirs(dirPath)

        filePath = f"{dirPath}/{time}.png"

        f = open(filePath, "wb")
        f.write(data)
        f.close()