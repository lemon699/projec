from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from OP_Page.po_page.Base import Base
from OP_Page.po_page.contact_page import contact


class add_member(Base):
    __ele_username=(By.ID,"username")
    __ele_acctid=(By.ID,"memberAdd_acctid")
    __ele_phone=(By.ID,"memberAdd_phone")
    __ele_save=(By.LINK_TEXT,"保存")

    def add_mb(self, username, acctid, phone):
        self.find(self.__ele_username).send_keys(username)
        self.find(self.__ele_acctid).send_keys(acctid)
        self.find(self.__ele_phone).send_keys(phone)
        self.find(self.__ele_save).click()
        sleep(3)
        return contact(self.driver)
    def add_mb_fail(self, username, acctid, phone):
        self.find(self.__ele_username).send_keys(username)
        self.find(self.__ele_acctid).send_keys(acctid)
        self.find(self.__ele_phone).send_keys(phone)
        self.find(self.__ele_save).click()
        tips=self.driver.find_elements(By.CSS_SELECTOR,".ww_inputWithTips_tips")
        tips_list = [ele.text for ele in tips]
        sleep(3)
        return tips_list
