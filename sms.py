from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import ElementSMS
import Element
import re
import sys

from ElementTips import login_page_tips


class SMS:
    def __init__(self, driver):
        self.element = Element.Element_version
        self.driver = driver
    def getCode(self, language, getCode_fillCode):
        # 根据传入的参数决定是否点击获取验证码
        if getCode_fillCode[0]:
            # 点击获取验证码
            if language == "English":
                print("当前语言为英文")
                self.driver.find_element(by='xpath', value=self.element.En_CodeLogin_GetCode).click()
                print("已发送验证码")
                self.driver.implicitly_wait(1)
                # 判断是否存在用户
                rt = self.user_exist_judge()
                if rt:
                    print("即将退出程序")
                    sys.exit()
                else:
                    print("即将进入 readCode 进程")
                    self.readCode()
            elif language == "Chinese":
                print("当前语言为中文")
                self.driver.find_element(by='xpath', value=self.element.Ch_CodeLogin_Get).click()
                print("已发送验证码")
                self.driver.implicitly_wait(1)
                # 判断是否存在用户
                rt = self.user_exist_judge()
                if rt:
                    print("即将退出程序")
                    sys.exit()
                else:
                    self.readCode()
            else:
                print("未传入language参数!")
            # 开始从通知栏获取短信验证码
            print("即将进入 readCode 进程")
            self.readCode()
        elif not getCode_fillCode[0]:
            return None
    def readCode(self):
        print("进入 readCode 进程")
        wait = WebDriverWait(self.driver, 30)
        print("打开通知栏")
        self.driver.open_notifications()
        print("通知栏已经打开并清除已有通知,开始获取验证码")
        self.driver.implicitly_wait(1)
        try:
            code = wait.until(EC.visibility_of_element_located((By.XPATH, ElementSMS.sms_code)))
            if code:
                print("验证码获取成功")
                print(code.text)
                pattern = r"验证码为：(\d+)"
                verify_code = re.search(pattern, code.text).group(1)
                print(f"验证码为:{verify_code}")
                if verify_code:
                    print("即将关闭通知栏")
                    # 清除通知栏内容防止下次获取验证码时读取到以前的验证码
                    self.driver.find_element(by='id', value=ElementSMS.notification_clear).click()
                    print("通知栏已关闭")
                    self.driver.implicitly_wait(1)
                    return str(verify_code)
                else:
                    print("验证码获取失败，未能正则匹配到验证码")
                print("下一步操作关闭通知栏")
            else:
                print("验证码获取失败，我找到对应元素")
        except TimeoutError:
            print("超时，未找到元素")
        print("按下返回键")

    def user_exist_judge(self):
        print("执行用户存在判断")
        var = login_page_tips["Ch_NoSuchUserTip"]
        print(var)
        try:
            user_exist = self.driver.find_element(by='xpath', value=var)
            txt = user_exist.get_attribute("content-desc")
            print(txt)
            if user_exist:
                print("用户不存在")
                return txt
            else:
                print("等待验证码")
        except NoSuchElementException:
            print(self.driver.contexts)




