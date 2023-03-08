import calculator

def test_print():
    assert calculator.print_function("hello")  

def test_fun1():
    assert calculator.function_1(2, 3)== 5

def test_fun1():
    assert calculator.function_2(5, 2)== 3
