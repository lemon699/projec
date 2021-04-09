
import pytest

from Calculator import Calculator


class Testcal:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect",[
        (1,1,2),(0.2,0.2,0.4),(1.1,1.1,2.2),(0,22,22)
    ])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)
    @pytest.mark.parametrize("a,b,expect",[
        [1,2,0.5],[10,0.5,20],[0,2,0],[10,0,"除数不能为零"]
    ])
    def test_div(self,a,b,expect):
        assert expect == self.calc.div(a,b)
    @pytest.mark.parametrize("a,b,expect",[
        [1,1,1],[0.1,2,0.2],[0,10,0],[10,10,100]
    ])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        [1,1,0], [0,2,-2], [0.2,0.1,0.1], [10,0.1,9.9]
    ])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)