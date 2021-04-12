import pytest
import yaml

def getdatas():
    with open("./datas.yaml") as f:
        datas = yaml.safe_load(f)
        return datas

class Testcal:

    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # @pytest.mark.parametrize("a,b,expect",getdatas()["int_datas"],ids=getdatas()["ids"])
    @pytest.mark.last
    def test_add(self,initcal,getint):
        assert getint[2] == round(initcal.add(getint[0],getint[1]),2)


    # @pytest.mark.parametrize("a,b,expect",getdatas()["div_datas"],ids=getdatas()["ids"])
    @pytest.mark.first
    def test_div(self,initcal,getdiv):
        try:
            assert getdiv[2] == initcal.div(getdiv[0],getdiv[1])
        except ZeroDivisionError:
            print("除数为零")