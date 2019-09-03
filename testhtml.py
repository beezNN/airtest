
#引入webdriver和unittest所需要的包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

#引入HTMLTestRunner包
import HTMLTestRunner
chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)

class Baidu(unittest.TestCase):
    #初始化设置
    def setUp(self):
        self.driver = browser
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu(self):
        driver = self.driver
        driver.get("http://www.baidu.com/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Selenium Webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

        # is_element_present函数用来查找页面元素是否存在
        def is_element_present(self, how, what):
            try:
                self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    # 对弹窗异常的处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True



if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()

    #将测试用例，加入到测试容器中
    test.addTest(Baidu("test_baidu"))

    #定义个报告存放的路径，支持相对路径
    file_path = "D:\\Zhongw\\htmltestrunner\\result.html"
    file_result= open(file_path, 'wb')

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"百度搜索测试报告", description = u"用例执行情况")

    #运行测试用例
    runner.run(test)
    file_result.close()