#1.打开浏览器
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost/index.php?m=user&c=public&a=login")

driver.find_element_by_id("username").send_keys("df001")

driver.find_element_by_id("password").send_keys("123456")

driver.find_element_by_class_name("login_btn").click()




#2：打开登陆页面
#3；