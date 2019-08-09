from sense_hat import SenseHat

class SensorService:
    def __init__(self):
        self.sensors = SenseHat()
        self.sensors.clear()

    def getPressure(self):
        return self.sensors.get_pressure()

    def getTemperature(self):
        return self.sensors.get_temperature()

    def getHumidity(self):
        return self.sensors.get_humidity()

    def getOrientation(self):
        for i in range(0,20):
            orientation = self.sensors.get_orientation()

        return orientation
