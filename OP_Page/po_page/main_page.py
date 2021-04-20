
from OP_Page.po_page.Base import Base
from OP_Page.po_page.depart_page import add_depart
from OP_Page.po_page.member_page import add_member


class main_p(Base):

    def click_contact(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        return add_depart(self.driver)
    def click_add_member(self):
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        return add_member(self.driver)


