from selenium.webdriver.common.by import By

from OP_Page.po_page.Base import Base
from OP_Page.po_page.contact_page import contact


class add_depart(Base):
    __add=(By.CSS_SELECTOR,".member_colLeft_top_addBtnWrap")
    __adddepart=(By.CSS_SELECTOR,".js_create_party")
    __name=(By.NAME,"name")
    __clickselect=(By.CSS_SELECTOR,".js_parent_party_name")
    __select=(By.CSS_SELECTOR,".qui_dialog_body.ww_dialog_body [id='1688853873144684_anchor']")
    __submit=(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')
    __js_tips=(By.ID,'js_tips')
    def add_depart(self,departname):
        self.find(self.__add).click()
        self.find(self.__adddepart).click()
        self.find(self.__name).send_keys(departname)
        self.find(self.__clickselect).click()
        self.find(self.__select).click()
        self.find(self.__submit).click()
        return contact(self.driver)


    def add_depart_fail(self,departname):
        self.find(self.__add).click()
        self.find(self.__adddepart).click()
        self.find(self.__name).send_keys(departname)
        self.find(self.__clickselect).click()
        self.find(self.__select).click()
        self.find(self.__submit).click()
        tips=self.find(self.__js_tips)
        return tips.text



