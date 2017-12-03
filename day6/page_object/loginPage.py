from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):     #构造方法;实例化LoginPage对象的时候，需要把driver作为参数传进来，便于别的属性和方法使用driver
        self.driver = driver

    title = "道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"

    username_input_loc = (By.ID,"username") #小括号表示元组，，元组有两个元素，第一个元素是控件的定位方式；第二个元素是，控件定位方式的具体值

    password_input_loc = (By.ID,"password")

    login_button_loc = (By.CLASS_NAME,"login_btn")

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()


    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        #self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element(*self.username_input_loc).send_keys(username)
        #星号作用就是把一个元组中的元素分别传入方法的参数中
        #前面加星号，表示传入就不是元组，而是元组中的两个元素
    def input_password(self,password):
        #self.driver.find_element_by_id("password").send_keys(password)
        #self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(*self.password_input_loc).send_keys(password)
