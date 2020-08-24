from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():  # TO DO
    with pytest.raises(ValueError) as exp:
        Point("X", 12.111, -555)
    assert str(exp.value) == 'Invalid latitude and longitude combination'


def test_invalid_city_name():
    with pytest.raises(ValueError) as exp:
        Point(123, 10, 10)
    assert str(exp.value) == 'City name must be a string'
