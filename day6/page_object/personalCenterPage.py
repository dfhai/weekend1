

class PersonalCenterPage:
    #网页是基于浏览器打开的，不能在一个页面创建浏览器，所以要浏览器的使用权，即需要把driver传进来
    def __init__(self,driver):
        self.driver = driver

    title = "我的会员中心 - 道e坊商城 - Powered by Haidao"
