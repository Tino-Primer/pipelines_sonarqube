from operator import truediv


def my_app(num):
    if num > 0:
        return True
    else:
        return False

def duplicate_my_app(num):
    if num > 0:
        return True
    else:
        return False

def poor_code():
    # foo is not defined
    foo()
    print("poor code")