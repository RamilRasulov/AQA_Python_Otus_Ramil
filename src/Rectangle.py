

class Rectangle:
        def __init__(self, side_a, side_b):
                if side_a <= 0 or side_b <= 0:
                        raise ValueError("Can not create Rectangle")
                self.side_a = side_a
                self.side_b = side_b
                self.name = f"Rectangle {side_a} and {side_b}"
                self.area = self.get_area()
                self.perimeter = self.get_perimeter()

        def get_area(self):
                return self.side_a * self.side_b


        def get_perimeter(self):
                return 2 * (self.side_a + self.side_b)


