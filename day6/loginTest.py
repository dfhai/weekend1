import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #打开网页
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        #可读性好点，如下：
        lp = LoginPage(self.driver)    #实例化一个登陆页面
        lp.open()



        #登陆
        #self.driver.find_element(By.ID,"username").send_keys("df001")
        #self.driver.find_element(By.ID,"password").send_keys("123456")
        #self.driver.find_element(By.CLASS_NAME,"login_btn").click()
        lp.input_username("df001")
        lp.input_password("123456")
        lp.click_login_button()

        #断言
        #expected = "我的会员中心"
        #time.sleep(5)
        #self.assertIn("我的会员中心",self.driver.title)
        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title,self.driver.title)