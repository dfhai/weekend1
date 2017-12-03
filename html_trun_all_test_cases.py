import os
import smtplib
import unittest
#HTMLTestRunner是基于unittest框架的一个扩展，可以自己在网上自行下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
     f = open(path, 'rb')  #读html报告文件内容，作为邮件正文
     mail_body = f.read()     #邮件正文
     f.close()
     #要想发邮件，需把二进制的内容转成MIME格式
     #MIME  multipurse多用途  Internet互联网    Mail邮件   Extension扩展
     #MIME是对邮件协议的一个扩展，让邮件不仅支持文件，还支持多种格式，比如图片，音频，二进制文件等
     msg = MIMEText(mail_body,'html','utf-8')
     #邮件正文外，还要主题，发件人，收件人
     '''
     msg是字典的类型，类似于数组
     '''
     msg['Subject'] = Header("自动化测试报告",'utf-8')
      #注：如果想用客户端软件或者自己写代码登陆邮箱，很多类型的邮件需要单独设置一个客户短授权码——为了邮箱安全
     msg['From'] = 'bwftest126@126.com'
     msg['To'] = 'dennis147@126,com'

     #开始发邮件：
     '''
     1.打开登陆页面，即链接邮箱服务器
     （连接服务器时，先必须搞清楚网络传输协议，
     发邮件的协议，一般有三种，查看自己邮箱支持的协议；
     126邮箱支持pop3,smtp,imap三种，所以可以用smtp发）
     2.登陆邮箱
     3.发送邮件
     4.退出邮箱
     '''
     #导入smtplib的代码库
     smtp = smtplib.SMTP() #实例化一个smtp类对象
     smtp.connect("smtp.126.com")

     #登陆邮箱
     smtp.login('bwftest126@126.com','abc123asd654')

     #发送邮件
     smtp.sendmail('bwftest126@126.com', 'dennis147@126,com', msg.as_string())
     #msg是MIME类型，需要转换成str类型

     #退出邮箱
     smtp.quit()
     print("email has sent out!")


if __name__ == '__main__':
   #时间戳
   #strftime  str是String   f是format格式  ，通过该方法定义时间格式
   now = time.strftime("%Y-%m-%d_%H-%M-%S")
   #Y year年, m month月，d day日 ，
   suite = unittest.defaultTestLoader.discover('./day5', '*Test.py')
   #HTMLTestRunner    html测试用例运行器,它最终会生成一个html格式的测试报告
   #我们需要指定报告存放路径
   #sys.stdout表示系统标准输出（二进制文件）
   base_path = os.path.dirname(__file__)
   path = base_path + "/report/report" + now + ".html"
   file = open(path, 'wb')
   HTMLTestRunner( stream=file, title="海盗商城测试报告", description="测试环境：window server 2008 + Chrome").run(suite)
   #括号里的参数名可以不写，只写参数值（传参的顺序必须固定）
   file.close()
   #把html报告作为邮件正文，发邮件
   send_mail(path)
   #生成的测试报告，只显示类名和方法名，只能给专业人士看
   #我们应该相关的手动测试用例的标题加到我们的测试报告
   #我们自动化测试用例是从手工测试用例中挑出来的，手工测试用例怎么写，我们就怎么写编写代码,我们的代码应该体现手工测试用例的标题
'''
新的测试报告会覆盖原来的测试报告，如果想把所有的测试保存，则要加个时间戳：按照当前时间计算一个数字，把数字作为文件名的一部分，避免了文件名重复的问题
'''
#生成测试报告后，当测试用例全部执行完成，应该生成一封提醒邮件，通知其他关注人员
