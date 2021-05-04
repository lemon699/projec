from faker import Faker

from APP_test.app_page.app import APP


class Testapp:
    def setup_class(self):
        self.faker = Faker("zh-CN")

    def setup(self):
        self.app=APP()
        self.main=self.app.start().goto_MainPage()

    def teardown(self):
        self.app.stop()

    def test_appwx(self):
        name,phone=self.faker.name(),self.faker.phone_number()
        self.main.goto_contact().goto_addmember().goto_editmember().goto_addmemberpage(name,phone).success()

    def test_delmember(self):
        self.main.goto_contact().goto_editmember().goto_editpage().delmember()
