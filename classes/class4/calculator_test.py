from calculator import square

def test_square():   
    assert square(2) == 4
    assert square(9) == 81

def test_negative():
    assert square(-6) != 12
    assert square(-8) == 64

def test_zero():
    assert square(0) == 0
    