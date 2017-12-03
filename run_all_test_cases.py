import unittest


if __name__ == '__main__':
    #默认的测试用例加载器,用于寻找符合一定规则的测试用例
    #discover发现
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #执行suite中所有的测试用例
    #TextTestRunner 文本的测试用例运行器

    '''
    TextTestRunner 首字母大写，说明它是一个类，类不能直接调用方法
    python中要实例化才能调用方法
    python中实例化方法是在类后面加（），不需要new关键字
    '''
    unittest.TextTestRunner().run(suite)

    '''
    执行结果    ..
    表示第一个和第二个都执行成功，如果为F表示执行失败
    '''
