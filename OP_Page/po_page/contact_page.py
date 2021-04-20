from selenium.webdriver.common.by import By

from OP_Page.po_page.Base import Base


class contact(Base):
    __mem=(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
    __depart=(By.CSS_SELECTOR,".jstree-anchor")
    def member_list(self):
        #拿到名字的元素列表
        elements=self.finds(self.__mem)
        memlist = [ele.text for ele in elements]
        return memlist
    def depart_list(self):
        #拿到部门的元素列表
        elements=self.finds(self.__depart)
        departlist = [ele.text for ele in elements]
        return departlist
