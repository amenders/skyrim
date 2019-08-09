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
