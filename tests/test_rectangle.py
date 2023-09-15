from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ("side_a", "side_b", "area", "perimeter"),
    [(8, 10, 80, 36), (2, 4, 8, 12)],
)
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b", "area", "perimeter"),
    [(-8, -10, 80, -36), (0, 0, 0, 0), (2, 4, 8, 12)],
)
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter
