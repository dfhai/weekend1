import unittest

import time


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("df002")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("userpassword2").send_keys("123456")
        driver.find_element_by_name("mobile_phone").send_keys("15236536536")
        driver.find_element_by_name("email").send_keys("1471@qq.com")
        driver.find_element_by_name("reg_btn").click()
        #检查数据库中新增记录
        expected = "df002"
        time.sleep(3)
        actual = connDb()[1]