from src.mathoperation import add,sub,mul,div

def test_add():
    assert add(1,2)==3
    assert add(2,5)==7

def test_sub():
    assert sub(4,2)==-2
    assert sub(5,2)==3

def test_mul():
    assert mul(1,2)==2
    assert mul(2,5)==10

def test_div():
    assert div(8,2)==4
    assert div(10,2)==5