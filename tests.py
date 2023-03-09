"""import calcul"""
import Calculator

def test_print():
    """test_print"""
    assert Calculator.print_function("hello") 

def test_fun1():
    """test_fun1"""
    assert Calculator.function_1(2, 3)== 5

def test_fun2():
    """test_fun2"""
    assert Calculator.function_2(5, 2)== 3
