#通讯录页面
from appium.webdriver.common.mobileby import MobileBy

from APP_test.app_page.addmember_page import AddMemberPage
from APP_test.app_page.base_page import Base
from APP_test.app_page.editmember_page import EditMemberPage


class ContactListPage(Base):
    __editm=(MobileBy.ID,"com.tencent.wework:id/h8l")

    def goto_addmember(self):
        # 点击添加成员
        self.swipe_find("添加成员").click()
        return AddMemberPage(self.driver)

    def goto_editmember(self):
        #点击编辑按钮
        self.find(*self.__editm).click()
        return EditMemberPage(self.driver)