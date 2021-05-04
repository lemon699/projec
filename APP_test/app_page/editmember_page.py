#编辑成员页面
from appium.webdriver.common.mobileby import MobileBy

from APP_test.app_page.base_page import Base


class EditMemberPage(Base):
    __name_ele=(MobileBy.XPATH, "//*[@text='姓名　']/..//*[@text='必填']")
    __phone_ele=(MobileBy.XPATH, "//*[@text='手机　']/..//*[@text='必填']")
    __save_ele=(MobileBy.XPATH, "//*[@text='保存']")
    __edits = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ftg']")
    __confirm = (MobileBy.XPATH, "//*[@text='确定']")
    __me_ele=(MobileBy.XPATH,"//*[@text='无法删除自己']")
    __back_ele=(MobileBy.ID,"com.tencent.wework:id/h86")
    def goto_addmemberpage(self,name,phone):
        from APP_test.app_page.addmember_page import AddMemberPage
        # 输入name和phone
        self.find(*self.__name_ele).send_keys(name)
        self.find(*self.__phone_ele).send_keys(phone)
        # 点击保存
        self.find(*self.__save_ele).click()
        return AddMemberPage(self.driver)

    def goto_editpage(self, x=0):
        edits_ele = self.finds(*self.__edits)
        edits_ele[x].click()
        return self

    def delmember(self):
        #点击删除成员
        self.swipe_find("删除成员").click()
        #判断是否为管理员
        if self.__me_ele:
            self.find(*self.__confirm).click()
            self.find(*self.__back_ele).click()
            self.goto_editpage(1)
            self.swipe_find("删除成员").click()
            self.find(*self.__confirm).click()
        else:
            self.find(*self.__confirm).click()




