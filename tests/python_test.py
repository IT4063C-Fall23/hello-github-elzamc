import pytest
import numpy as np
import math
from testbook import testbook


@pytest.fixture(scope="module")
def tb():
    with testbook("./python-exercises.ipynb", execute=True) as tb:
        yield tb


def test_demo(tb):
    add = tb.ref("simple_add")
    assert add(1, 2) == 3
    assert add(2, 3) == 5

def test_exercise1(tb):
    is_even_or_odd = tb.ref("is_even_or_odd")
    try:
        even_numbers = (2,4,6,8,10)
        odd_numbers = (1,3,5,7,9)
        for num in even_numbers:
            assert is_even_or_odd(num) == "even", "❌ Expected {} to be labelled even".format(num)
        for num in odd_numbers:
            assert is_even_or_odd(num) == "odd", "❌ Expected {} to be labelled odd".format(num)
    except AssertionError as e:
        print(e)

def test_exercise2(tb):
    is_leap_year = tb.ref("is_leap_year")
    try:
        leap_years = (2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048)
        not_leap_years = (2005, 2009, 2013, 2017, 2021, 2025, 2029, 2033, 2037, 2041, 2045, 2049)
        for year in leap_years:
            assert is_leap_year(year) == True, "❌ Expected {} to be a leap year".format(year)
        for year in not_leap_years:
            assert is_leap_year(year) == False, "❌ Expected {} to be a not leap year".format(year)
    except AssertionError as e:
        print(e)


def test_exercise3(tb):
    convert_celsius_to_fahrenheit = tb.ref("convert_celsius_to_fahrenheit")
    try:
        assert convert_celsius_to_fahrenheit(0) == 32, "❌ Expected 0ºC to be 32ºF"
        assert convert_celsius_to_fahrenheit(10) == 50, "❌ Expected 10ºC to be 50ºF"
        assert convert_celsius_to_fahrenheit(25) == 77, "❌ Expected 25ºC to be 72ºF"
    except AssertionError as e:
        print(e)

def test_exercise4(tb):
    get_area_and_circumference_of_circle = tb.ref("get_area_and_circumference_of_circle")
    try:
        area2, circum2 = get_area_and_circumference_of_circle(1)
        assert (
            math.isclose(area2, 3.14, abs_tol=0.01) == True
        ), "❌ Expected area of circle of radius 1 to be 3.14 not {}".format(area2)
        assert (
            math.isclose(circum2, 6.28, abs_tol=0.01) == True
        ), "❌ Expected circumference of circle of radius 1 to be 6.28 not {}".format(
            circum2
        )

        area3, circum3 = get_area_and_circumference_of_circle(3)
        assert (
            math.isclose(area3, 28.27, abs_tol=0.01) == True
        ), "❌ Expected area of circle of radius 3 to be 28.27 not {}".format(area3)
        assert (
            math.isclose(circum3, 18.84, abs_tol=0.01) == True
        ), "❌ Expected circumference of circle of radius 3 to be 18.8 not {}".format(
            circum3
        )

    except AssertionError as e:
        print(e)

def test_exercise5(tb):
    fizzbuzz = tb.ref("fizzbuzz")
    try:
        assert fizzbuzz(25) == [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz",16,17,"Fizz",19,"Buzz","Fizz",22,23,"Fizz"]
    except AssertionError as e:
        print(e)