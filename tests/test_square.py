from src.circle import Circle
from src.square import Square, Rectangle
import pytest


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(10,100,40),
                          (7,49,28)])
def test_square(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == f"Rectangle {side_a} and {side_a}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(-10, 100, 40),
                          (0, 49, 28)])
def test_square(side_a, area, perimeter):
    with pytest.raises(ValueError):
        Square(side_a)
    

def test_add_area():
    r = Rectangle(8,10)
    s = Square(10)
    assert r.add_area(s) == 180

def test_add_area_negative():
    r = Rectangle(8, 10)
    c = Circle(2)
    assert c.add_area(r) == 92.56637061435917