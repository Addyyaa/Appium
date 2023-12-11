from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import ElementSMS
import Element
import re
import sys
import logging

from ElementTips import login_page_tips


class SMS:

    def __init__(self, driver):
        self.element = Element.Element_version
        self.driver = driver
        self.logger = logging.getLogger(__name__)
    def getCode(self, language, getCode_fillCode):
        # 根据传入的参数决定是否点击获取验证码
        if getCode_fillCode[0]:
            # 点击获取验证码
            if language == "English":
                self.logger.info("当前语言为英文")
                self.driver.find_element(by='xpath', value=self.element.En_CodeLogin_GetCode).click()
                self.logger.info("已发送验证码")
                self.driver.implicitly_wait(1)
                # 判断是否存在用户
                rt = self.user_exist_judge()
                if rt:
                    self.logger.info("即将退出程序")
                    sys.exit()
                else:
                    self.logger.info("即将进入 readCode 进程")
                    code = self.readCode()

                    if getCode_fillCode[1] is None:
                        self.logger.info("验证码为空")
                        code = ""
                    elif getCode_fillCode[1] == "non-custom":
                        self.logger.info(f"验证码为:{code}")
                    else:
                        code = getCode_fillCode[1]
                        # 填写验证码
                    self.driver.find_element(by='xpath', value=self.element.En_CodeLogin_Code).send_keys(code)
                    self.logger.info(f"填写的验证吗为{code}")
            elif language == "Chinese":
                self.logger.info("当前语言为中文")
                self.driver.find_element(by='xpath', value=self.element.Ch_CodeLogin_Get).click()
                self.logger.info("已发送验证码")
                self.driver.implicitly_wait(1)
                # 判断是否存在用户
                rt = self.user_exist_judge()
                if rt:
                    self.logger.info("即将退出程序")
                    sys.exit()
                else:
                    code = self.readCode()
                    if getCode_fillCode[1] is None:
                        self.logger.info("验证码为空")
                        code = ""
                    elif getCode_fillCode[1] == "non-custom":
                        self.logger.info(f"验证码为:{code}")
                    else:
                        code = getCode_fillCode[1]
                    # 填写验证码
                    self.driver.find_element(by='xpath', value=self.element.Ch_CodeLogin_CodeInput).send_keys(code)
                    self.logger.info(f"填写的验证吗为{code}")
            else:
                self.logger.info("未传入language参数!")
        # TODO 不获取验证码的情况下的逻辑处理
        elif not getCode_fillCode[0]:
            # 不填写验证码直接点击登录
            pass
            # 填写错误的验证码
            pass

    def readCode(self):
        self.logger.info("进入 readCode 进程")
        wait = WebDriverWait(self.driver, 30)
        self.logger.info("打开通知栏")
        self.driver.open_notifications()
        self.logger.info("通知栏已经打开并清除已有通知,开始获取验证码")
        self.driver.implicitly_wait(1)
        try:
            code = wait.until(ec.visibility_of_element_located((By.XPATH, ElementSMS.sms_code)))
            if code:
                self.logger.info("验证码获取成功")
                self.logger.info(code.text)
                self.logger.info(code.text)
                pattern = r"证码为：(\d+)"
                verify_code = re.search(pattern, code.text).group(1)
                self.logger.info(f"验证码为:{verify_code}")
                if verify_code:
                    self.logger.info("即将关闭通知栏")
                    # 清除通知栏内容防止下次获取验证码时读取到以前的验证码
                    self.driver.find_element(by='id', value=ElementSMS.notification_clear).click()
                    self.logger.info("通知栏已关闭")
                    self.driver.implicitly_wait(1)
                    return str(verify_code)
                else:
                    self.logger.error("验证码获取失败，未能正则匹配到验证码")
            else:
                self.logger.error("验证码获取失败，未找到对应元素")
        except TimeoutError as e:
            self.logger.error("TimeoutError: %s", e)
        self.logger.info("按下返回键")

    def user_exist_judge(self):
        self.logger.info("执行用户存在判断")
        var = login_page_tips["Ch_NoSuchUserTip"]
        self.logger.info(var)
        try:
            user_exist = self.driver.find_element(by='xpath', value=var)
            txt = user_exist.get_attribute("content-desc")
            self.logger.info(txt)
            self.logger.info("开始判断用户存在元素")
            self.logger.info("开始判断用户存在元素")
            if user_exist:
                self.logger.warning("用户不存在")
                return txt
            else:
                self.logger.info("等待验证码")
        except NoSuchElementException as e:
            self.logger.error("NoSuchElementException: %s. Contexts: %s", e, self.driver.contexts, exc_info=True)




