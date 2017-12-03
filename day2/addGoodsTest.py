#登陆
from selenium import webdriver
from selenium.webdriver import ActionChains`

driver = webdriver.Chrome()
driver.implicitly_wait(30)  #犯错：不加时会报错

driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
#商品管理
driver.find_element_by_link_text("商品管理").click()
#添加商品
driver.find_element_by_link_text("添加商品").click()

#商品名称
#商品管理和添加商品属于页面根节点的网页
#商品名称属于frame框架里的子网页，所以需要切换页面
driver.switch_to.frame("mainFrame")     #切换到子框架页面
driver.find_element_by_name("name").send_keys("iphone X")

#商品分类
driver.find_element_by_id(1).click()
driver.find_element_by_link_text("手机配件").click()
driver.find_element_by_id("6").click()

ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
#提交