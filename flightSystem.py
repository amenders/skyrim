from services.FileSystemService import FileSystemService
from services.SensorService import SensorService

sensors = SensorService()

file = FileSystemService("/home/pi/Desktop/data/log.txt", "/home/pi/Desktop/data/log.txt")

while (True):
    pressure = sensors.getPressure()
    temp = sensors.getTemperature()
    humidity = sensors.getHumidity()

    logText = "press: {0}; temp: {1}; humi: {2}".format(pressure, temp, humidity)

    file.log(logText)

    
