from src.my_app import my_app, poor_code, bad_bad_code
from src.new_file import *


def test_num_more_than_zero():
    assert my_app(5) == True

def test_num_less_than_zero():
    assert my_app(-2) == False

def test_num_is_zero():
    assert my_app(0) == False

def test_num_is_float():
    assert my_app(0.5) == True

def test_poor_code():
    assert poor_code() == "poor code"

def test_bad_bad_code():
    assert bad_bad_code() == "bad bad code"

def test_new_func():
    assert tino_new_func() == "hello"
