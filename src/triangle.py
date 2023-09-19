from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <=0:
            if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
                raise ValueError("Can not create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a=}, {side_b=} and {side_c=}"


    def get_area(self):
        semi_perimeter = self.get_perimeter() / 2
        return (
                semi_perimeter
                * (semi_perimeter - self.side_a)
                * (semi_perimeter - self.side_b)
                * (semi_perimeter - self.side_c)
        )**0.5

    def get_perimeter(self):
        return  self.side_a + self.side_b + self.side_c
