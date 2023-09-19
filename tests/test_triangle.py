import pytest
from src.triangle import Triangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area", "perimeter"),
    [(8, 10, 15, 36.98, 33), (5, 5, 5, 10.83, 15)],
)
def test_triangle(side_a, side_b, side_c, area, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == f"Triangle {side_a=}, {side_b=} and {side_c=}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area", "perimeter"),
    [(-8, -10, 80, -36, 90), (0, 0, 0, 2, -1)],
)
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
