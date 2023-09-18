from src.circle import  Circle
from src.square import Square
from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(8,10,80,36),
                          (2,4,8,12)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-8,-10,80,-36),
                          (0,0,0,0),
                          (2,4,8,12)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(10,100,40),
                          (7,49,28)])
def test_rectangle(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == f"Square {side_a}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


def test_add_area():
    r = Rectangle(8,10)
    s = Square(10)
    assert r.add_area(s) == 180


def test_add_area_negative():
    r = Rectangle(8,10)
    c = Circle (20)
    assert r.add_area(r) == 160

