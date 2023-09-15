from abc import ABC, abstractmethod
from src.rectangle import Rectangle


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise AssertionError("Can not add area")
        return self.get_area() + other_figure.get_area()

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Can not create Rectangle")
        self.side_a = side_a
        self.side_b = side_b
        self.name = f"Rectangle {side_a} and {side_b}"

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    class Square(Rectangle):
        def __init__(self, side_a):
            if side_a <= 0:
                raise ValueError("Can not create Square")
            super().__init__(side_a, side_a)
            self.side_a = side_a
            self.name = f"Square {side_a}"


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def get_area(self):
        return
