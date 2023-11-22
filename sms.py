from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import ElementSMS
import re
class SMS:
    def __init__(self, driver):
        self.driver = driver
    def getCode(self):
        wait = WebDriverWait(self.driver, 30)
        print("打开通知栏")
        self.driver.open_notifications()
        print("通知栏已经打开,开始获取验证码")
        try:
            code = wait.until(EC.visibility_of_element_located((By.XPATH, ElementSMS.sms_code)))
            if code:
                print("验证码获取成功")
                pattern = r"验证码为：(\d+)"
                verify_code = re.search(pattern, code.text)
                if verify_code:
                    return verify_code
                else:
                    print("验证码获取失败，未能正则匹配到验证码")
            else:
                print("验证码获取失败，我找到对应元素")
        except TimeoutError:
            print("超时，未找到元素")
        self.driver.press_keycode(4)

