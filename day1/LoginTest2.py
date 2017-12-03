#1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")

#2.点击登陆链接
driver.find_element_by_link_text("登录").click()
#从浏览器的所有窗口中，排除第一个窗口，剩下第二个窗口
#把selenium切花到第二个窗口
cwh = driver.current_window_handle
whs = driver.window_handles
#item 表示集合中的一个元素
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window("item")

#输入用户名和密码
driver.find_element_by_id("username").send_keys("df001")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("login_btn").click()
