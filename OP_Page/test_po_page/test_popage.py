import pytest

from OP_Page.Datas.test_data import test_datas
from OP_Page.po_page.main_page import main_p


class TestPopage():
    def setup_class(self):
        self.main_a = main_p()

    @pytest.mark.parametrize("username,acctid,phone",test_datas("../Datas/member.yaml"),ids=["test1","test2","test3"])
    def test_add_member(self,username,acctid,phone):
        # 添加成员测试
        namelist=self.main_a.click_add_member().add_mb(username, acctid, phone).member_list()
        assert username in namelist

    @pytest.mark.parametrize("username,acctid,phone",[("user4","111","19999999999")],ids=["test1"])
    def test_add_member_fail(self,username,acctid,phone):
        # 添加成员失败测试
        #拿到add_mb_fail return的tips列表
        errtipslist=self.main_a.click_add_member().add_mb_fail(username, acctid, phone)
        err=[i for i in errtipslist if i !=""]
        assert "user3" in err[0]

    @pytest.mark.parametrize("departname",test_datas("../Datas/depart.yaml"),ids=["test1","test2","test3"])
    def test_add_depart(self,departname):
        #添加部门测试
        namelist=self.main_a.click_contact().add_depart(departname).depart_list()
        assert departname in namelist

    def test_add_depart_fail(self):
        #添加部门失败测试
        tipselement=self.main_a.click_contact().add_depart_fail("测试部门1")
        assert "该部门已存在" in tipselement

        
