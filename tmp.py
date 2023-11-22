from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'Redmi Note 10 Pro',
    # 'udid': '99001756422713',
    'appPackage': 'com.android.mms',
    'appActivity': '.ui.MmsTabActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 10)

# # 等待应用启动
# driver.implicitly_wait(10)
# # 同意协议
# driver.find_element(by='xpath',
#                     value='//android.widget.Button[@resource-id="com.ost.pintura:id/btn_custom_privacy_sure"]').click()
# driver.implicitly_wait(10)
# # 选择地域
# driver.find_element(by='xpath', value='//android.webkit.WebView[@text="pages/area[2]"]/android.view.View[1]').click()
# driver.find_element(by='xpath', value='//android.widget.TextView[@text="美国"]').click()
# # 选择语言
# driver.find_element(by='xpath', value='//android.widget.TextView[@text="简体中文"]').click()
# driver.find_element(by='xpath', value='//android.widget.TextView[@text="English"]').click()
# driver.implicitly_wait(10)
# driver.find_element(by='xpath', value='//android.widget.TextView[@text="Confirm"]').click()
# driver.implicitly_wait(10)
# # 通过邮箱登录
# loginType = driver.find_element(by='xpath', value='//android.view.View[@content-desc="Email"]')
# loginType.click()
# # 输入邮箱账号
# emai = driver.find_element(by='xpath', value='//android.widget.EditText[@text="Please enter your email"]')
# emai.send_keys('2698567570@qq.com')
# # 输入密码
# password = driver.find_element(by='xpath', value='//android.widget.EditText[@text="Please enter your password"]')
# password.click()
# password.send_keys('sf19960408')
# driver.hide_keyboard()
# driver.implicitly_wait(10)
# # 判断用户协议是否勾选
# userAgreement = driver.find_element(by='xpath',
#                                     value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ImageView')
# if userAgreement.is_selected():
#     pass
# else:
#     userAgreement.click()
# # 点击登录
# driver.find_element(by='xpath', value='//android.view.View[@content-desc="Sign in"]').click()
# # 执行完测试后，关闭应用
# time.sleep(10)
# driver.quit()
