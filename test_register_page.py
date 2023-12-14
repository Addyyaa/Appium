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
        # 进入注册界面
        driver.find_element(by='xpath', value=element.Ch_LoginPage_Register).click()
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
        driver.quit()

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
        setup["driver"].implicitly_wait(1)
        try:
            code = wait.until(ec.visibility_of_element_located((By.XPATH, ElementSMS.sms_code)))
            if code:
                setup["logger"].info("验证码获取成功")
                setup["logger"].info(code.text)
                pattern = r"证码为：(\d+)"
                verify_code = re.search(pattern, code.text).group(1)
                setup["logger"].info(f"验证码为:{verify_code}")
                if verify_code:
                    setup["logger"].info("即将关闭通知栏")
                    # 清除通知栏内容防止下次获取验证码时读取到以前的验证码
                    setup["driver"].find_element(by='id', value=ElementSMS.notification_clear).click()
                    setup["logger"].info("通知栏已关闭")
                    setup["driver"].implicitly_wait(1)
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
            logging.info("已勾选用户协议")
        else:
           logging.info("不进行用户协议勾选")

    # 每条用例执行前和执行后需要做的处理
   @pytest.fixture
    def function_setup(self, setup):
    # 清理通知栏
        setup["driver"].open_notifications()
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='id', value=ElementSMS.notification_clear).click()
        logging.info("通知栏内容已清理")
        setup["driver"].implicitly_wait(1)

    # 中文国内手机注册流程
    def chlanguage_chregion_phone_regist(self, setup, get_verify_code=True, read_sms_code=True, is_check_user_agreement=True):
        wait = WebDriverWait(setup["driver"], 5)
        setup["logger"] = logging.getLogger(__name__)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_AreaCodeList).click()
        setup["logger"].info("已展开区号列表")
        sleep(1)
        self.area_code_click(setup)
        setup["logger"].info("已点击搜索框")
        setup["driver"].implicitly_wait(10)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_AreaCode_Search).send_keys(
            setup["code_text"])
        setup["logger"].info("已发送搜索文本")
        setup["driver"].hide_keyboard()
        setup["logger"].info("已关闭虚拟键盘")
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_86).click()
        setup["logger"].info("已选择区号")
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_PhoneNumber).click()
        setup["driver"].implicitly_wait(1)
        setup["logger"].info("已点击手机号输入框")
        # 由于文本框不支持sendkeys，所以使用虚拟键盘输入
        self.virtural_keyboard_input(setup, data=setup["phone"])
        setup["logger"].info("已输入手机号")
        setup["driver"].hide_keyboard()
        setup["logger"].info("已关闭虚拟键盘")
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Nickname).send_keys(setup["nick_name"])
        setup["logger"].info("已输入昵称")
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Passwd).send_keys(setup["phone_password"])
        setup["logger"].info("已输入密码")
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_ConfirmPasswd).send_keys(
            setup["phone_confirm_password"])
        setup["logger"].info("已输入确认密码")
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Region).click()
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_RegionChina).click()
        if get_verify_code == True:
            # 点击发送验证码
            setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_GetCode).click()
            setup["logger"].info("已点击获取验证码")
            logging.info("即将获取提示元素")
            logging.info(setup["tips_element"]["Ch_sendCodeTip"])
            code_sent = wait.until(ec.visibility_of_element_located((By.XPATH, setup["tips_element"]["Ch_sendCodeTip"])))
            tip_text = code_sent.text
            logging.info(tip_text)
            if setup["phone"] == "":
                logging.info("请输入手机号")
                excepted_result = "请输入手机号"
            else:
                is_valid = self.phone_format_check(setup["phone"], setup["country_code"])
                logging.info(is_valid)
                if is_valid:
                    if setup["is_registered"]:
                        excepted_result = "手机号或邮箱已存在"
                        logging.info("手机号或邮箱已存在")
                        assert tip_text == excepted_result, "提示内容不正确"
                        logging.info("断言已完成,即将退出程序")
                        pytest.skip("断言成功，跳过测试")
                    else:
                        excepted_result = "验证码已发送"
                        logging.info("验证码已发送")
                        assert tip_text == excepted_result, "提示内容不正确"
                else:
                    excepted_result = "请输入正确的手机号码"
                    logging.info("请输入正确的手机号")
                    assert tip_text == excepted_result, "提示内容不正确"
                    pytest.skip("断言成功，跳过测试")
            logging.info("断言已完成")
            # 根据参数判断是否要读取短信验证码
            if read_sms_code:
                # 需要从通知栏获取验证码
                logging.info("开始读取短信验证码")
                verify_code = self.get_sms_verify_code(setup)
                logging.info(f"短信验证码读取完成，验证码为：{verify_code}")
                # 如果用户想要使用自定义的验证码，则重新赋值便可
                setup["verify_code"] = verify_code
            logging.info("开始填写验证码")
            setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_CodeInput).click()
            self.virtural_keyboard_input(setup, data=setup["verify_code"])
            logging.info("已输入获取的短信验证码")
        else:
            setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_CodeInput).click()
            self.virtural_keyboard_input(setup, data=setup["verify_code"])
            logging.info("未获取短信验证码但已输入自定义验证码")
        setup["driver"].hide_keyboard()
        logging.info("已关闭虚拟键盘")
        setup["driver"].implicitly_wait(1)
        self.user_agreement_handle(setup, is_check_user_agreement)
        # 点击注册按钮
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_RegisterButton).click()
        setup["logger"].info("已点击注册按钮")
        # 获取弹窗元素
        try:
            tip = setup["wait"].until(
                ec.visibility_of_element_located((By.XPATH, setup["tips_element"]["Ch_sendCodeTip"])))
            if tip:
                tip_text = tip.text
                logging.info(tip_text)
                setup["logger"].info("注册成功")
                assert tip_text == Config.Config.register_success_excepted_result, f"提示内容错误，应提示：" \
                                                                                   f"{Config.Config.register_success_excepted_result}，实际提示：{tip_text}"
            else:
                setup["logger"].error("获取元素失败")
        except selenium.common.exceptions.TimeoutException as e:
            logging.error(f"获取元素超时")
            setup["logger"].error("TimeoutError: %s", e)

    # 用例1：正确输入所有信息
    def test_chlanguage_chregion_phone_regist(self, setup):
        setup["phone"] = "15250996938"
        setup["is_registered"] = True
        self.chlanguage_chregion_phone_regist(setup)

    # 用例2
    def test_12(self):
        print("test12")





# class TestEnglishRegisterPage:
#     def __init__(self):
#         setup["driver"] = Init.get_driver()
#         self.version = VersionSelection.VersionSelection(setup["driver"])
#         self.version.version_selection("Chinese", "English")