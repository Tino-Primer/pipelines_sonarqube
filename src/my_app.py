from operator import truediv


def my_app(num):
    if num > 0:
        return True
    else:
        return False

# duplicated code - test and delete
def my_app(num):
    if num > 0:
        return True
    else:
        return False

# foo is not defined - test and delete
def poor_code():
    foo()
    print("poor code")