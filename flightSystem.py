from services.LogService import LogService
from services.SensorService import SensorService
from services.CameraService import CameraService

camera = CameraService("/home/pi/Desktop/mymovie.mjpeg")

camera.takeVideo(6)
