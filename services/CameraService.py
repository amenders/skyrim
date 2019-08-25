from picamera import PiCamera
from time import sleep
from multiprocessing import Process

def recordProcess(duration, path, count):
    camera = PiCamera()
    camera.start_recording("{0}/video_{1}_working.h264".format(path, count))
    sleep(duration)
    camera.stop_recording()

class CameraService:

    def __init__(self, _storagePath):
        self.imageCount = 0
        self.imagePath = _storagePath + "/images"
        self.videoPath = _storagePath + "/videos"
        #self.camera = PiCamera()
        self.imageCount = 0
        self.videoCount = 0

    def takePicture(self):
        self.camera.capture("{0}/image_{1}.jpg".format(self.imagePath, self.imageCount))
        self.imageCount += 1

    def takeVideo(self, duration):
        action = Process(target=recordProcess, args=(duration, self.videoPath, self.videoCount))
        action.start()
        action.join()

        
