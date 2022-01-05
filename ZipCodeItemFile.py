import math

from typing import Tuple, List

Coordinates = Tuple[float, float]

class ZipcodeItem:

    def __init__(self,zip, lat, long, x, y):
        self.zip = zip
        self.lat = lat
        self.long = long
        self.x = x
        self.y = y
        self.attractor_number = 0

    def distanceSquaredToPoint(self,pt: Coordinates) -> float:
        return math.pow(pt[0]-self.x,2)+math.pow(pt[1]-self.y,2)

    def findClosestAttractor(self, attractor_list: List[Coordinates])-> int:
        N = len(attractor_list)
        closest_index = 0
        closest_distance_squared = 9999999999.0
        for i in range(N):
            d2 = self.distanceSquaredToPoint(attractor_list[i])
            if (d2 < closest_distance_squared):
                closest_index = i
                closest_distance_squared = d2

        return closest_index


