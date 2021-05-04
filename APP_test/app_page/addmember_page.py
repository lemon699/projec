#添加成员页面
from appium.webdriver.common.mobileby import MobileBy

from APP_test.app_page.base_page import Base


class AddMemberPage(Base):
    __add_ele=(MobileBy.XPATH, "//*[@text='手动输入添加']")
    __success_ele=(MobileBy.XPATH, "//*[@text='添加成功']")
    def goto_editmember(self):
        from APP_test.app_page.editmember_page import EditMemberPage
        # 点击手动输入
        self.find(*self.__add_ele).click()
        return EditMemberPage(self.driver)
    def success(self):
        self.find(*self.__success_ele)