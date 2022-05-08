import time
import os
from datetime import datetime

class Repository:

    def store(self, data):
        name = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        f = open(f"{os.getcwd()}/images/{name}.png", "wb")
        f.write(data)
        f.close()