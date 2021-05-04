#主页

from appium.webdriver.common.mobileby import MobileBy

from APP_test.app_page.base_page import Base
from APP_test.app_page.contact_page import ContactListPage


class MainPage(Base):
    __contact_ele=(MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_contact(self):
        #click 通讯录
        self.find(*self.__contact_ele).click()
        return ContactListPage(self.driver)