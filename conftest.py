import pytest
from Calculator import Calculator
from test_Calculator import getdatas


@pytest.fixture(scope="class")
def initcal():
    #setup
    print("开始计算")
    calc = Calculator()
    yield calc
    #teardown
    print("计算结束")

@pytest.fixture(params=getdatas()["int_datas"],ids=getdatas()["ids"])
def getint(request):
    return request.param

@pytest.fixture(params=getdatas()["div_datas"],ids=getdatas()["ids"])
def getdiv(request):
    return request.param
