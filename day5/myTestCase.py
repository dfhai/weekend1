import unittest
from selenium import  webdriver

#方法和包名空两行
class MyTestCase(unittest.TestCase):
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()    #浏览器版本必须和driver的驱动版本匹配才能窗口最大化

    def tearDown(self):
        self.driver.quit()