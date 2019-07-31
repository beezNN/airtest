__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 通过ADB连接本地Android设备
connect_device("Android:b3c4dc01")
#安装待测软件apk，路径信息。
# install("path/to/your/apk")
#开始运行app
start_app("com.ddread")
#点击某个图片，Airtest中基于图像识别语法，图片自己提供。
# touch(Template("image_of_a_button.png"))
#滑动语音，开头图片跟结尾图片
# swipe(Template("slide_start.png"), Template("slide_end.png"))
#添加断言的图片
# assert_exists(Template("success.png"))
#点击Android上的返回键
#keyevent("BACK")
#点击Android上的Home键返回
#home()
#uninstall("package_name_of_your_apk")

# poco("com.ddread:id/img_random_read").click()
# for i in range(1000):
#     touch(([950,1100]))
#     sleep(0.5)
# poco("android.widget.ImageView").click()
# sleep(3)
# poco("com.ddread:id/id_tv_add_shelf").click()
# sleep(3)
# poco("com.ddread:id/id_tv_add_shelf").click()
# poco("com.ddread:id/id_img_toolbar_back").click()
# poco("com.ddread:id/id_img_shelf").click()