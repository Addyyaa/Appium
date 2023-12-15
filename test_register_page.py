import re
import selenium.common.exceptions
import Init
import Element
import ElementTips
import Config
import pytest
import logging
from selenium.webdriver.common.by import By
import VersionSelection
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import phonenumbers
import ElementSMS


class TestChineseRegisterPage:
    @classmethod
    @pytest.fixture(scope="class")
    def setup(cls):
        driver = Init.get_driver()
        # 先进行一次返回防止通知栏已打开的情形
        driver.press_keycode(4)
        version = VersionSelection.VersionSelection(driver)
        version.version_selection("Chinese", "Chinese")
        element = Element.Element_version
        tips_element = ElementTips.register_page_tips
        is_registered = Config.Config.is_registered
        # 账号及密码
        email = Config.Config.email
        email_password = Config.Config.email_password
        email_confirm_password = Config.Config.email_confirm_password
        phone = Config.Config.phone
        # 国家码为CN、US等等
        country_code = Config.Config.country_code
        phone_password = Config.Config.phone_password
        phone_confirm_password = Config.Config.phone_confirm_password
        nick_name = Config.Config.nick_name
        code_text = Config.Config.area_code_searchtext
        # TODO 需要对验证码重新设计，验证码输入、不输入、没点击获取验证码
        verify_code = Config.Config.verify_code
        # 设置全局的隐式等待时间
        driver.implicitly_wait(5)
        # 进入注册界面
        try:
            driver.find_element(by='xpath', value=element.Ch_LoginPage_Register).click()
        except selenium.common.exceptions.NoSuchElementException:
            logging.error("没有找到进入注册页面按钮")
        logger = logging.getLogger(__name__)
        wait = WebDriverWait(driver, 5)
        yield {
            "driver": driver,
            "element": element,
            "tips_element": tips_element,
            "is_registered": is_registered,
            "email": email,
            "email_password": email_password,
            "email_confirm_password": email_confirm_password,
            "phone": phone,
            "country_code": country_code,
            "phone_password": phone_password,
            "phone_confirm_password": phone_confirm_password,
            "nick_name": nick_name,
            "verify_code": verify_code,
            "code_text": code_text,
            "logger": logger,
            "wait": wait
        }
        print("类夹具的打印")
        sleep(3)
        driver.quit()

    # 每条用例执行前和执行后需要做的处理
    @pytest.fixture
    def function_setup(self, setup):
        self.is_clear = False
        # 清理通知栏
        setup["driver"].open_notifications()
        setup["logger"].info("已打开通知栏")
        is_exist = self.find_notification_clear(setup)
        if is_exist is not None:
            is_exist.click()
            setup["logger"].info("通知栏内容已清理")
        else:
            setup["driver"].press_keycode(4)
            setup["logger"].info("没有可清理的内容，退出通知栏")
        yield
        if not self.is_clear:
            self.find_phone_number_input(setup).clear()
            setup["logger"].info("已清理手机号码")
            self.find_register_nickname_input(setup).clear()
            setup["logger"].info("已清理昵称")
            self.find_register_phone_passwd(setup).clear()
            setup["logger"].info("已清理密码")
            self.find_register_phone_confirmpasswd(setup).clear()
            setup["logger"].info("已清理确认密码")
            self.find_register_phone_verifycode(setup).clear()
            setup["logger"].info("已清理验证码")
        else:
            setup["logger"].info("注册成功，无需清理输入框！")

    def find_notification_clear(self, setup):
        driver = W
        try:
            # 显式等待，等待元素可见
            setup["logger"].info("开始查找")
            element = WebDriverWait(setup["driver"], 1).until(
                ec.visibility_of_element_located((By.ID, ElementSMS.notification_clear))
            )
            return element
        except selenium.common.exceptions.TimeoutException:
            setup["logger"].error("元素未在规定时间内可见")
            setup["logger"].info("查找结束")
            return None


    def find_register_phone_verifycode(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_CodeInput)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_register_phone_confirmpasswd(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_ConfirmPasswd)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_register_phone_passwd(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Passwd)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")
    def find_register_nickname_input(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Nickname)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_phone_number_input(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_PhoneNumber)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    # 手机区号根据x、y点击
    def area_code_click(self, setup):
        x = 500
        y = 1090
        touch = TouchAction(setup["driver"])
        touch.tap(x=x, y=y).perform()

    # 手机格式校验
    def phone_format_check(self, phone_number, country_code):
        try:
            parsed_number = phonenumbers.parse(phone_number, country_code)
            is_valid_number = phonenumbers.is_valid_number(parsed_number)
            return is_valid_number
        except phonenumbers.NumberParseException as e:
            logging.error(f"号码解析异常{e}")
            return False

    # 从通知栏获取短信验证码
    def get_sms_verify_code(self, setup):
        wait = WebDriverWait(setup["driver"], 30)
        setup["logger"].info("开始获取短信验证码")
        setup["driver"].open_notifications()
        setup["logger"].info("通知栏已打开")
        try:
            code = wait.until(ec.visibility_of_element_located((By.XPATH, ElementSMS.sms_code)))
            if code:
                setup["logger"].info("验证码获取成功")
                setup["logger"].info(code.text)
                pattern = r"码为：(\d+)"
                verify_code = re.search(pattern, code.text).group(1)
                setup["logger"].info(f"验证码为:{verify_code}")
                if verify_code:
                    setup["logger"].info("即将关闭通知栏")
                    # 清除通知栏内容防止下次获取验证码时读取到以前的验证码
                    self.find_notification_clear(setup).click()
                    setup["logger"].info("通知栏已关闭")
                    return str(verify_code)
                else:
                    setup["logger"].error("验证码获取失败，未能正则匹配到验证码")
            else:
                setup["logger"].error("验证码获取失败，未找到对应元素")
        except selenium.common.exceptions.TimeoutException as e:
            logging.error(f"获取验证码超时")
            setup["logger"].error("TimeoutError: %s", e)

    # 虚拟键盘输入(数字)
    def virtural_keyboard_input(self, setup, data):
        for digit in data:
            digit = int(digit)
            key_code = digit + 7  # 转换成对应的键码
            setup["driver"].press_keycode(key_code)

    # 用户协议处理
    def user_agreement_handle(self, setup, is_check_user_agreement):
        if is_check_user_agreement:
            setup["driver"].find_element(by='xpath', value=setup["element"].Ch_UserAgreement).click()
            setup["logger"].info("已勾选用户协议")
        else:
           setup["logger"].info("不进行用户协议勾选")

    # 中文国内手机注册流程
    def chlanguage_chregion_phone_regist(self, setup, get_verify_code=True, read_sms_code=True, is_check_user_agreement=True):
        wait = WebDriverWait(setup["driver"], 5)
        self.find_register_phone_area_list(setup).click()
        setup["logger"].info("已展开区号列表")
        sleep(1)
        self.area_code_click(setup)
        setup["logger"].info("已点击搜索框")
        self.find_register_phone_areacode_search(setup).send_keys(
            setup["code_text"])
        setup["logger"].info("已发送搜索文本")
        setup["driver"].hide_keyboard()
        setup["logger"].info("已关闭虚拟键盘")
        self.find_register_phone_86code(setup).click()
        setup["logger"].info("已选择区号")
        self.find_phone_number_input(setup).click()
        setup["logger"].info("已点击手机号输入框")
        # 由于文本框不支持sendkeys，所以使用虚拟键盘输入
        self.virtural_keyboard_input(setup, data=setup["phone"])
        setup["logger"].info("已输入手机号")
        setup["driver"].hide_keyboard()
        setup["logger"].info("已关闭虚拟键盘")
        self.find_register_nickname_input(setup).send_keys(setup["nick_name"])
        setup["logger"].info("已输入昵称")
        self.find_register_phone_passwd(setup).send_keys(setup["phone_password"])
        setup["logger"].info("已输入密码")
        self.find_register_phone_confirmpasswd(setup).send_keys(
            setup["phone_confirm_password"])
        setup["logger"].info("已输入确认密码")
        self.find_register_phone_region(setup).click()
        self.find_register_phone_china_region(setup).click()
        if get_verify_code == True:
            # 点击发送验证码
            self.find_register_phone_getcode(setup).click()
            setup["logger"].info("已点击获取验证码")
            setup["logger"].info("即将获取提示元素")
            setup["logger"].info(setup["tips_element"]["Ch_sendCodeTip"])
            code_sent = wait.until(ec.visibility_of_element_located((By.XPATH, setup["tips_element"]["Ch_sendCodeTip"])))
            tip_text = code_sent.text
            setup["logger"].info(tip_text)
            if setup["phone"] == "":
                setup["logger"].info("请输入手机号")
                excepted_result = "请输入手机号"
            else:
                is_valid = self.phone_format_check(setup["phone"], setup["country_code"])
                setup["logger"].info(is_valid)
                if is_valid:
                    if setup["is_registered"]:
                        excepted_result = "手机号或邮箱已存在"
                        setup["logger"].info("手机号或邮箱已存在")
                        assert tip_text == excepted_result, "提示内容不正确"
                        setup["logger"].info("断言已完成,即将退出程序")
                        pytest.skip("断言成功，跳过测试")
                    else:
                        excepted_result = "验证码已发送"
                        setup["logger"].info("验证码已发送")
                        assert tip_text == excepted_result, "提示内容不正确"
                else:
                    excepted_result = "请输入正确的手机号码"
                    setup["logger"].info("请输入正确的手机号")
                    assert tip_text == excepted_result, "提示内容不正确"
                    pytest.skip("断言成功，跳过测试")
            setup["logger"].info("断言已完成")
            # 根据参数判断是否要读取短信验证码
            if read_sms_code:
                # 需要从通知栏获取验证码
                setup["logger"].info("开始读取短信验证码")
                verify_code = self.get_sms_verify_code(setup)
                setup["logger"].info(f"短信验证码读取完成，验证码为：{verify_code}")
                # 如果用户想要使用自定义的验证码，则重新赋值便可
                setup["verify_code"] = verify_code
            setup["logger"].info("开始填写验证码")
            self.find_register_phone_verifycode(setup).click()
            self.virtural_keyboard_input(setup, data=setup["verify_code"])
            setup["logger"].info("已输入获取的短信验证码")
        else:
            self.find_register_phone_verifycode(setup).click()
            self.virtural_keyboard_input(setup, data=setup["verify_code"])
            setup["logger"].info("未获取短信验证码但已输入自定义验证码")
        setup["driver"].hide_keyboard()
        setup["logger"].info("已关闭虚拟键盘")
        self.user_agreement_handle(setup, is_check_user_agreement)
        # 点击注册按钮
        self.find_register_phone_register_button(setup).click()
        setup["logger"].info("已点击注册按钮")
        # 获取弹窗元素
        try:
            tip = setup["wait"].until(
                ec.visibility_of_element_located((By.XPATH, setup["tips_element"]["Ch_sendCodeTip"])))
            if tip:
                tip_text = tip.text
                setup["logger"].info(tip_text)
                setup["logger"].info("注册成功")
                assert tip_text == Config.Config.register_success_excepted_result, f"提示内容错误，应提示：" \
                                                                                   f"{Config.Config.register_success_excepted_result}，实际提示：{tip_text}"
                # 此处设置变量是为了注册成功时终止情况输入框操作
                self.is_clear = True
            else:
                setup["logger"].error("获取元素失败")
        except selenium.common.exceptions.TimeoutException as e:
            logging.error(f"获取元素超时")
            setup["logger"].error("TimeoutError: %s", e)

    def find_register_phone_register_button(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_RegisterButton)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_register_phone_getcode(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_GetCode)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_register_phone_china_region(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_RegionChina)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_register_phone_region(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Region)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_register_phone_86code(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_86)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_register_phone_areacode_search(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_AreaCode_Search)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    def find_register_phone_area_list(self, setup):
        try:
            return setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_AreaCodeList)
        except selenium.common.exceptions.NoSuchElementException:
            setup["logger"].error("未找到对应元素")

    # 用例1：正确输入所有信息
    def test_chlanguage_chregion_phone_regist(self, setup, function_setup):
        setup["phone"] = "15250996938"
        setup["is_registered"] = False
        self.chlanguage_chregion_phone_regist(setup)




    # 用例2
    def test_12(self):
        print("test12")





# class TestEnglishRegisterPage:
#     def __init__(self):
#         setup["driver"] = Init.get_driver()
#         self.version = VersionSelection.VersionSelection(setup["driver"])
#         self.version.version_selection("Chinese", "English")