from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import By
# 初始化Appium驱动
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '13',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.tencent.mm',  # 启动APP Package名称
    'appActivity': 'com.tencent.mm.ui.LauncherUI',  # 启动Activity名称
    'noReset': True,  # 不要重置App
    "chromedriverExecutable": "D:\微信小程序自动化\chromedriver.exe"  # 指定chrome.driver驱动位
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)
sleep(5)
# 滑动屏幕
size = driver.get_window_size()
start_x, start_y = size['width'] * 0.5, size['height'] * 0.2
end_x, end_y = size['width'] * 0.5, size['height'] * 0.9
duration = 200
TouchAction(driver).press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release().perform()
#点击优一尚选
driver.find_element(By.XPATH, '//android.widget.RelativeLayout[@content-desc="优一尚选,"]').click()
print(driver)
sleep(5)

a=driver.find_element(By.XPATH,'//android.widget.RelativeLayout[@content-desc="抽奖,"]')
print(a)

# 点击搜索框
#element = driver.find_element(By.XPATH,'//*[@id="1719f248--featureSearchBar"]/wx-view/wx-view')
#TouchAction(driver).tap(element).perform()
sleep(3)
# 关闭驱动
driver.quit()