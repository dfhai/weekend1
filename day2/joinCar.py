import time
from selenium import webdriver

# 45版本一下的filefox浏览器，不需要驱动文件
# 从46版本以上的firefox浏览器，也需要把driver.exe文件放到环境变量下面
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)  # 隐式等待最大时间30s
driver.maximize_window()  # 窗口最大化
driver.get("http://localhost")

login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')", login_link)  # 犯错：removeAttribute拼写错误
login_link.click()
driver.find_element_by_id("username").send_keys("df001")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("username").submit()

driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()

#iphone_image = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
iphone_link = "div.shop_01-imgbox > a"
#driver.find_element_by_css_selector(iphone_link).click()

driver.find_element_by_css_selector(iphone_link)
iphone = driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')", iphone)
iphone.click()

#点击加入购物车
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
driver.find_element_by_class_name("add-address").click()

#填写收货地址
driver.find_element_by_name("address[address_name]").send_keys("df")
driver.find_element_by_name("address[mobile]").send_keys("15035623653")

sheng = driver.find_element_by_id("add-new-area-select")
#Select(sheng).select_by_value("110000")
Select(sheng).select_by_value("130000")

shi = driver.find_elements_by_tag_name("select")[1]    #犯错：这里要用elements，通过select一类条件中查找
Select(shi).select_by_index(1)

qu = driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_index(2)





