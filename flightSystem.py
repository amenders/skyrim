from services.FileSystemService import FileSystemService
from services.SensorService import SensorService
from time import sleep

sensors = SensorService()

file = FileSystemService("/home/pi/Desktop/data/log.txt", "/home/pi/Desktop/data/log.txt")

while (True):
    orientation = sensors.getOrientation()

    

    sleep(1)

    
