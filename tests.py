"""import TpClass"""
from devopstp import TpClass

def test_print():
    """test_print"""
    assert TpClass.function_0(6,3)==3

def test_fun1():
    """test_fun1"""
    assert TpClass.function_1(2,3) == 5

def test_fun2():
    """test_fun2"""
    assert TpClass.function_2(5,2) == 3
