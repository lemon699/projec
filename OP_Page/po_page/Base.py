# 重复步骤分离出来进行封装
from time import sleep

import yaml
from selenium import webdriver


class Base():
    #base_driver是用来子类继承Base,传入self.driver用来判断
    def __init__(self,base_driver=None):
        if base_driver==None:
            self.driver = webdriver.Chrome()
            # 打开企业微信的登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            # 添加序列化cookies登录到企业微信
            with open("../test_po_page/cookies_data", encoding="UTF-8") as f:
                cookiesdata = yaml.safe_load(f)
            for cookies in cookiesdata:
                self.driver.add_cookie(cookies)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(5)
        else:
            self.driver=base_driver

    def find(self,by,ele=None):
        if ele==None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by,ele)

    def finds(self,by,ele=None):
        if ele==None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by,ele)

