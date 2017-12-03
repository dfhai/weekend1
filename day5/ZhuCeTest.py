#封装了myTestCase,再写测试用例，不需要再写setUp和tearDown方法
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    #3个双引号，表示文档字符串；也是一种注释
    #和#号的区别：这种注释可以打印在页面上
    """注册功能测试用例"""
    #因为MyTestCase已经实现了setup和teatdown方法，我们再写测试用例就不要重新实现setup和teatdown方法
    def test_ZhuCe(self):
        """打开注册页面"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        #断言方法：
        #1）driver.current_url  #用来获取当前浏览器中的网址
        #2）driver.title        #用来获取当前浏览中的标签页的title
        actual = driver.title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        #get_screenshot_as_file  #截取图片
        base_path = os.path.dirname(__file__) #当前脚本路径
        print(base_path)
        path = base_path.replace('day5','report/image/')    #括号里的参数是将当前脚本存放路径替换为图片存放路径
        driver.get_screenshot_as_file(path + "zhuce.png")       #path + "zhuce.png" 表示在path路径中创建png图片
        self.assertEqual(actual, expected)
