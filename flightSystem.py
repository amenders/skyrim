from services.LogService import LogService
from services.SensorService import SensorService
from services.CameraService import CameraService

camera = CameraService("/home/pi/Desktop/skyrim/data")

camera.takeVideo(5)

