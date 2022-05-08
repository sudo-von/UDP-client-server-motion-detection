import time
import os
from datetime import datetime

class Repository:

    def store(self, data):
        datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S").split(' ')
        date, time = datetime

        dirPath = f"{os.getcwd()}/images/{date}"
        dirExist = os.path.exists(dirPath)
        if !dirExist:
            os.makedirs(dirPath)

        filePath = f"{dirPath}/{time}.png"

        f = open(filePath, "wb")
        f.write(data)
        f.close()