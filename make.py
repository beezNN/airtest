import unittest
import HTMLTestRunner
import time
import os

class make(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        print("构造函数")

    def test_aaa(self):
        print("aaa")
        self.assertEqual(1, 2)

    def test_bbb(self):
        print("bbb")
        self.assertEqual(2, 2)

    def test_ccc(self):
        print("ccc")
        self.assertEqual(3, 2)

if __name__ == '__main__':
    print("main-start")
    s = unittest.TestSuite()  # 实例化
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(make))  # 加载用例
    now = time.strftime('%Y-%m-%d %H%M%S')
    print("main-getcwd")
    filename = open(os.getcwd() + '/testResult_report' + now + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=filename,
        title='单元测试报告',
        description='单元测试报告',
        tester='youreyebows')
    runner.run(s)
    print("main-stop")