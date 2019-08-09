from datetime import datetime

class FileSystemService:

    def __init__(self, LogFile, ImageDirectory):
        self.logFile = LogFile
        self.imageDirectory = ImageDirectory

    def log(self, text):
        with open(self.logFile, "a") as file:
            file.write("[{0}]: {1}\n".format(datetime.now(), text))
