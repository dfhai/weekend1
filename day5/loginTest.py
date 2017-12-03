import unittest
from selenium import  webdriver

#方法和包名空两行
class DengLuTest(unittest.TestCase):
    """登陆模块测试用例"""
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()    #浏览器版本必须和driver的驱动版本匹配才能窗口最大化

    def tearDown(self):
        self.driver.quit()

    def test_denglu(self):
        """登陆测试正常情况测试用例"""
        driver = self.driver #将成员变量赋值给局部变量
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("df001")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("password").submit()
        print("当前用户名：df001")

