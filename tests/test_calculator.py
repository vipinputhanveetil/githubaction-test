from src.calculator import add,sub,mul,div

def test_add():
    assert add(1,2)==3
    assert add(-1,2)==1

def test_sub():
    assert sub(5,4)==1

def test_mul():
    assert mul(5,3)==15

def test_div():
    assert div(6,2)==3
