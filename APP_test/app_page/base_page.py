#创建一个基类页面,封装一些基本方法
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)

class Base:
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def find(self,by,value):
        logging.info(by)
        logging.info(value)
        return self.driver.find_element(by,value)
    def finds(self,bys,values):
        logging.info(bys)
        logging.info(values)
        return self.driver.find_elements(bys, values)

    # 封装页面滑动方法
    def swipe_find(self, ele_text, num=3):
        # 默认查找3次，如果3次还未找到就抛出异常
        for i in range(num):
            if i == num - 1:
                raise NoSuchElementException(f"找了{i}次未找到")
            try:
                return self.driver.find_element(MobileBy.XPATH, f"//*[@text='{ele_text}']")
            except NoSuchElementException:
                print("未找到该元素,滑动页面")
                # 获取当前屏幕尺寸
                size = self.driver.get_window_size()
                start_x = size["width"] / 2
                start_y = size["height"] * 0.8
                end_x = start_x
                end_y = size["height"] * 0.2
                # 调用swipe函数，在1s内完成页面滑动
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
