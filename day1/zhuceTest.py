from selenium import webdriver
#打开主页面
driver = webdriver.Chrome()

driver.get("http://localhost/")

#切换到注册页面
cwh = driver.current_window_handle

whs = driver.window_handles

for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)

#输入用户名
driver.find_element_by_name("username").send_keys("df002")

#输入密码
driver.find_element_by_name("password").send_keys("123456")

#确认密码
driver.find_element_by_name("userpassword2").send_keys("123456")

#输入手机
driver.find_element_by_name("mobile_phone").send_keys("15035262365")

#输入email
driver.find_element_by_link_text("email").send_keys("123@qq.com")

#点击注册
driver.find_element_by_class_name("reg_btn").click()

