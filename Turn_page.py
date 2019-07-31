__author__ = "Administrator"
import unittest
from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 通过ADB连接本地Android设备
connect_device("Android:b3c4dc01")
start_app("com.ddread")


class Turn_page(unittest.TestCase):
    @staticmethod
    def test_turn():
        for i in range(1000):
            touch([950, 1100])
            sleep(0.5)


if __name__ == '__main__':
    unittest.main()
