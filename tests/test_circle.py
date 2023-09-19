from src.circle import  Circle
import pytest


@pytest.mark.parametrize(("radius", "area", "perimetr"),
                         [(25, 1963.4954084936207, 157.07963267948966),
                          (100, 31415.926535897932, 628.3185307179587)])
def test_circle(radius, area, perimetr):
    r = Circle(radius)
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


@pytest.mark.parametrize(("radius", "area", "perimetr"),
                         [(0,1800,555),
                          (-5, 55, 80)])
def test_circle_negative(radius, area, perimetr):
    with pytest.raises(ValueError):
        Circle(radius)
