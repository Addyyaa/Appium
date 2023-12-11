from selenium.common.exceptions import NoSuchElementException
from Element import Element_version
from sms import SMS
from Config import Config
from ElementTips import login_page_tips
import sys
from time import sleep
import logging

class LoginPage:
    logger = logging.getLogger(__name__)
    element = Element_version()

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.email = Config.email
        self.email_password = Config.email_password
        self.phone = Config.phone
        self.phone_password = Config.phone_password
        self.verify_code = Config.verify_code


    def login(self,getCode_fillCode, loginType="email", language=None, *agreement_verifycode):
        login_methods = {
            "email": self.login_email,
            "phone": self.login_mobile,
            "code": self.login_code
        }

        login_method = login_methods.get(loginType)
        if login_method == self.login_code:
            login_method(language, getCode_fillCode, *agreement_verifycode)
        elif login_method == self.login_email or login_method == self.login_mobile:
            login_method(language, *agreement_verifycode)
        else:
            self.logger.warn("无效的登录类型")

    # 判断用户协议是否被勾选，还需补充中英文版本的判断
    def userAgreementJudge(self, language, *agreement_verifycode):
        userAgreement = None
        if agreement_verifycode[0]:
            if language == "English":
                self.logger.info("检测到英文版本用户协议")
                self.logger.info(language)
                userAgreement = self.driver.find_element(by='xpath', value=self.element.En_UserAgreement)
            elif language == "Chinese":
                self.logger.info("检测到中文版本用户协议")
                userAgreement = self.driver.find_element(by='xpath', value=self.element.Ch_UserAgreement)
            else:
                self.logger.warn("请输入正确的语言")

            # 检查元素是否找到
            if userAgreement:
                self.logger.info("已找到用户协议元素")
                # 判断用户协议是否勾选
                if userAgreement.is_selected():
                    self.logger.info("用户协议已勾选")
                    pass
                else:
                    self.logger.info("用户协议未勾选，即将勾选")
                    userAgreement.click()
                    self.logger.info("用户协议已勾选")
            else:
                self.logger.warn("用户协议元素未找到")
        else:
            pass
        # 点击登录
        if language == "English":
            self.driver.find_element(by='xpath', value=self.element.En_LoginButton).click()
            self.logger.info("登录按钮已点击")
        elif language == "Chinese":
            self.driver.find_element(by='xpath', value=self.element.Ch_LoginButton).click()
            self.logger.info("登录按钮已点击")
        else:
            self.logger.warn("请输入正确的语言")

    def login_email(self, language, *agreement_verifycode):
        self.logger.info("已选择邮箱登录")
        if language == "Chinese":
            # 点击邮箱登录
            self.driver.find_element(by='xpath', value=self.element.Ch_Email_Login).click()
            # 输入邮箱
            self.logger.info("开始输入邮箱地址")
            self.driver.find_element(by='xpath', value=self.element.Ch_Email_Input).send_keys(self.email)
            self.logger.info("邮箱已输入")
            # 输入密码
            pswd = self.driver.find_element(by='xpath', value=self.element.Ch_Email_Passwd)
            pswd.click()
            self.logger.info("开始输入密码")
            pswd.send_keys(self.email_password)
            self.logger.info("密码已输入")
            self.driver.hide_keyboard()
            self.driver.implicitly_wait(10)
        elif language == "English":
            # 点击邮箱登录
            self.driver.find_element(by='xpath', value=self.element.En_Email_Login).click()
            # 输入邮箱
            self.logger.info("开始输入邮箱地址")
            self.driver.find_element(by='xpath', value=self.element.En_Email_Input).send_keys(self.email)
            self.logger.info("邮箱已输入")
            # 输入密码
            pswd = self.driver.find_element(by='xpath', value=self.element.En_Email_Passwd)
            pswd.click()
            self.logger.info("开始输入密码")
            pswd.send_keys(self.email_password)
            self.logger.info("密码已输入")
            self.driver.hide_keyboard()
            self.driver.implicitly_wait(10)
            # 根据是否传入agreement参数判断是否勾选用户协议
            self.userAgreementJudge(language, *agreement_verifycode)

    def get_current_region(self, language):
        if language == "English":
            if self.driver.find_elements(by='xpath', value=self.element.En_United_States_Region):
                currentRegion = "United States"
                return currentRegion
            elif self.driver.find_elements(by='xpath', value=self.element.En_China_Region):
                currentRegion = "China"
                return currentRegion
            else:
                self.logger.warn("未找到当前地域的元素")
        elif language == "Chinese":
            if self.driver.find_elements(by='xpath', value=self.element.Ch_United_States_Region):
                currentRegion = "美国"
                return currentRegion
            elif self.driver.find_elements(by='xpath', value=self.element.Ch_China_Region):
                currentRegion = "中国大陆"
                return currentRegion
            else:
                self.logger.warn("未找到当前地域的元素")

    def user_exist_judge(self):
        self.logger.info("执行用户存在判断")
        var = login_page_tips["Ch_NoSuchUserTip"]
        self.logger.info(var)
        try:
            user_exist = self.driver.find_element(by='xpath', value=var)
            txt = user_exist.get_attribute("content-desc")
            self.logger.info(txt)
            if user_exist:
                self.logger.warn("用户不存在")
                return txt
            else:
                self.logger.info("等待验证码")
        except NoSuchElementException as e:
            self.logger.error("NoSuchElementException: %s. Contexts: %s", e, self.driver.contexts, exc_info=True)

    # Code for email login

    def login_mobile(self, language, *agreement_verifycode):
        self.logger.info("已选择手机登录")
        if language == "English":
            self.logger.info("进入英文版登录")
            # 点击手机登录
            self.driver.find_element(by='xpath', value=self.element.En_Phone_Login).click()
            # 获取地域信息
            self.logger.info("开始获取地域信息")
            currentRegion = self.get_current_region(language)
            self.logger.info(f"当前地域：{currentRegion}")
            if currentRegion == "United States":
                # 选择手机区号
                self.logger.info("开始选择手机区号")
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_List).click()
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_Input).send_keys('USA')
                self.driver.implicitly_wait(1)
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_1).click()
                self.logger.info("手机区号已选择")
                # 输入手机号
                self.logger.info("开始输入手机号")
                self.driver.find_element(by='xpath', value=self.element.En_PhoneNumber).send_keys(self.phone)
                self.logger.info("手机号已输入")
                # 输入密码
                passwd = self.driver.find_element(by='xpath', value=self.element.En_Phone_Passswd)
                passwd.click()
                self.logger.info("开始输入密码")
                passwd.send_keys(self.phone_password)
                self.logger.info("密码已输入")
                self.driver.hide_keyboard()
            elif currentRegion == "China":
                # 选择手机区号
                self.logger.info("开始选择手机区号")
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_List).click()
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_Input).send_keys('china')
                self.driver.implicitly_wait(1)
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_86).click()
                self.logger.info("手机区号已选择")
                # 输入手机号
                self.logger.info("开始输入手机号")
                self.driver.find_element(by='xpath', value=self.element.En_PhoneNumber).send_keys(self.phone)
                self.logger.info("手机号已输入")
                # 输入密码
                passwd = self.driver.find_element(by='xpath', value=self.element.En_Phone_Passswd)
                passwd.click()
                self.logger.info("开始输入密码")
                passwd.send_keys(self.phone_password)
                self.logger.info("密码已输入")
                self.driver.hide_keyboard()
            else:
                self.logger.error("Please enter the correct region")
        elif language == "Chinese":
            self.logger.info("进入中文版登录")
            # 点击手机登录
            self.driver.find_element(by='xpath', value=self.element.Ch_Phone_Login).click()
            # 获取地域信息
            self.logger.info("开始获取地域信息")
            currentRegion = self.get_current_region(language)
            self.logger.info(f"当前地域：{currentRegion}")
            if currentRegion == "美国":
                # 选择手机区号
                self.logger.info("开始选择手机区号")
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_List).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_Code).send_keys('美国')
                self.driver.implicitly_wait(1)
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_Code_1).click()
                self.logger.info("手机区号已选择")
                # 输入手机号
                self.logger.info("开始输入手机号")
                self.driver.find_element(by='xpath', value=self.element.Ch_PhoneNumber).send_keys(self.phone)
                self.logger.info("手机号已输入")
                # 输入密码
                passwd = self.driver.find_element(by='xpath', value=self.element.Ch_Phone_Passswd)
                passwd.click()
                self.logger.info("开始输入密码")
                passwd.send_keys(self.phone_password)
                self.logger.info("密码已输入")
                self.driver.hide_keyboard()
            elif currentRegion == "中国大陆":
                # 选择手机区号
                self.logger.info("开始选择手机区号")
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_List).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_Code).send_keys('中国大陆')
                self.driver.implicitly_wait(1)
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_Code_86).click()
                self.logger.info("手机区号已选择")
                # 输入手机号
                self.logger.info("开始输入手机号")
                self.driver.find_element(by='xpath', value=self.element.Ch_PhoneNumber).send_keys(self.phone)
                self.logger.info("手机号已输入")
                # 输入密码
                passwd = self.driver.find_element(by='xpath', value=self.element.Ch_Phone_Passswd)
                passwd.click()
                self.logger.info("开始输入密码")
                passwd.send_keys(self.phone_password)
                self.logger.info("密码已输入")
                self.driver.hide_keyboard()
        else:
            self.logger.error("Please enter the correct language")
        # 根据传入的参数来决定是否勾选用户协议
        self.userAgreementJudge(language, *agreement_verifycode)

    def login_code(self, language, getCode_fillCode, *agreement_verifycode):
        sms = SMS(self.driver)
        self.logger.info("进入验证码登录")
        if language == "English":
            self.logger.info("进入英文版本登录")
            # 点击验证码登录
            self.driver.find_element(by='xpath', value=self.element.En_Code_Login).click()
            # 获取地域信息
            currentRegion = self.get_current_region(language)
            self.logger.info(f"当前地域：{currentRegion}")
            if currentRegion == "United States":
                self.logger.info("开始选择手机区号")
                # 选择手机区号
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_List).click()
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_Input).send_keys('USA')
                self.driver.implicitly_wait(1)
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_1).click()
                self.logger.info("手机区号已选择")
                # 输入手机号
                self.driver.find_element(by='xpath', value=self.element.En_PhoneNumber).send_keys(self.phone)
                self.driver.implicitly_wait(1)
            elif currentRegion == "China":
                self.logger.info("开始选择手机区号")
                # 选择手机区号
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_List).click()
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_Input).send_keys('china')
                self.driver.implicitly_wait(1)
                self.driver.find_element(by='xpath', value=self.element.En_AreCode_86).click()
                self.logger.info("手机区号已选择")
                # 输入手机号
                self.driver.find_element(by='xpath', value=self.element.En_PhoneNumber).send_keys(self.phone)
                self.driver.implicitly_wait(1)
        elif language == "Chinese":
            self.logger.info("进入中文版登录")
            # 点击验证码登录
            self.driver.find_element(by='xpath', value=self.element.Ch_Code_Login).click()
            # 获取地域信息
            currentRegion = self.get_current_region(language)
            self.logger.info(f"当前地域：{currentRegion}")
            if currentRegion == "美国":
                # 选择手机区号
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_List).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_Code).send_keys('美国')
                self.driver.implicitly_wait(1)
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_Code_1).click()
                self.logger.info("手机区号已选择")
                # 输入手机号
                self.driver.find_element(by='xpath', value=self.element.Ch_PhoneNumber).send_keys(self.phone)
                self.driver.implicitly_wait(1)
            elif currentRegion == "中国大陆":
                # 选择手机区号
                self.logger.info("开始选择手机区号")
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_List).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_Code).send_keys('中国大陆')
                self.driver.implicitly_wait(1)
                self.driver.find_element(by='xpath', value=self.element.Ch_Area_Code_86).click()
                self.logger.info("手机区号已选择")
                # 输入手机号
                self.driver.find_element(by='xpath', value=self.element.Ch_PhoneNumber).send_keys(self.phone)
                self.driver.implicitly_wait(1)
        sms.getCode(language, getCode_fillCode)
        # 根据传入的参数来决定是否勾选用户协议
        self.logger.info("开始校验用户协议")
        self.userAgreementJudge(language, *agreement_verifycode)
