from datetime import datetime

class LogService:

    def __init__(self, LogFile, header):
        self.logFile = LogFile

        with open(self.logFile, "a") as file:
            file.write("timestamp, {0}\n".format(header))
        

    def log(self, text):
        with open(self.logFile, "a") as file:
            file.write("{0}, {1}\n".format(datetime.now(), text))
