import math


class ZipcodeItem:

    def __init__(self,zip, lat, long, x, y):
        self.zip = zip
        self.lat = lat
        self.long = long
        self.x = x
        self.y = y
        self.attractor_number = 0



def distance_squared_between_zips(city1: ZipcodeItem, city2: ZipcodeItem) -> float:
    return math.pow(city1.x - city2.x, 2)+math.pow(city1.y - city2.y, 2)

