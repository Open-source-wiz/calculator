def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def test_divide():
    assert divide(6,2) == 3

def test_add():
    assert add(1,2) == 3

def test_multiply():
    assert multiply(2,3) == 6

def test_sub():
    assert sub(6,2) == 4