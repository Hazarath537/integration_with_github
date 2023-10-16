import my_functions

def test_square():
    assert my_functions.square(4) == 16
    assert my_functions.square(3) == 9

def test_factorial():
    assert my_functions.factorial(5) == 120
    assert my_functions.factorial(3) == 6

def test_cube():
    assert my_functions.cube(2) == 8
    assert my_functions.cube(3) == 27

