import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can not create Circle")
        self.radius = radius


    def get_area(self):
        return math.pi * (self.radius**2)

    def get_perimetr(self):
        return 2 * math.pi * self.radius