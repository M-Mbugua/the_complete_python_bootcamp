import math
class Line:
    def __init__(self, coor1, coor2):

        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):

        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2 - y1) / (x1 - x2)


class Cylinder:

    pi = 3.142

    def __init__(self, height=1, radius=1):

        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return Cylinder.pi * 2 * self.radius * (self.radius + self.height)



