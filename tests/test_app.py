from src.my_app import my_app


def test_num_more_than_zero():
    assert my_app(5) == True

def test_num_less_than_zero():
    assert my_app(-2) == False

def test_num_is_zero():
    assert my_app(0) == False

def test_num_is_float():
    assert my_app(0.5) == True
