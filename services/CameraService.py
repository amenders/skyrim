from picamera import PiCamera
from time import sleep
from multiprocessing import Process

class CameraService:

    def __init__(self, _storagePath):
        self.imageCount = 0
        self.storagePath = _storagePath
        self.camera = PiCamera()

    def takePicture(self):
        self.camera.capture(storagePath)

    def takeVideo(self, duration):
        video = Process(target=self.recordProcess, args=(self,duration,))
        video.start()
        video.join()

    def recordProcess(self, duration):
        self.camera.start_recording(self.storagePath)
        sleep(duration)
        self.camera.stop_recording()
        
