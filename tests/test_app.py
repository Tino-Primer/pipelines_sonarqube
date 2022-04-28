from src.my_app import my_app


def test_num_more_than_zero():
    my_app(5)

def test_num_less_than_zero():
    my_app(-1)

def test_num_is_zero():
    my_app(0)