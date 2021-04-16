# 使用序列化cookies登录企业微信并添加成员
from time import sleep
import yaml
from selenium import webdriver


class TestCookies:
    def test_addcookies(self):
        #chrome浏览器的复用
        opt=webdriver.ChromeOptions()
        opt.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        #打开登录后的企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #获取cookies并保存到data_yaml文件中
        cookies=self.driver.get_cookies()
        with open("./data_yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookies,f)
class TestLogin:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_addmember(self):
        #打开企业微信的登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        #添加序列化cookies登录到企业微信
        with open("./data_yaml",encoding="UTF-8") as f:
            cookiesdata=yaml.safe_load(f)
        for cookies in cookiesdata:
            self.driver.add_cookie(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #添加成员
        self.driver.find_element_by_link_text("通讯录").click()
        self.driver.find_element_by_link_text("添加成员").click()
        self.driver.find_element_by_id("username").send_keys("张三")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("123")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("18888888888")
        self.driver.find_element_by_link_text("保存").click()
        sleep(3)





