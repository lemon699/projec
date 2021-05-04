from appium import webdriver

from APP_test.app_page.base_page import Base
from APP_test.app_page.main_page import MainPage


class APP(Base):

    def start(self):
        if self.driver==None:
            caps = {
                "platformName": "android",
                "deviceName": "test",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self
    def restart(self):
        pass
    def stop(self):
        self.driver.quit()
    def goto_MainPage(self):
        return MainPage(self.driver)