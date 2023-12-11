import Init
import Element
import Config
import pytest
import logging
class TestRegisterPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        # 初始化 appium 连接操作
        driver = Init.get_driver()
        element = Element.Element_version
        # 账号及密码
        email = Config.Config.email
        email_password = Config.Config.email_password
        phone = Config.Config.phone
        phone_password = Config.Config.phone_password
        nick_name = Config.Config.nick_name
        # TODO 需要对验证码重新设计，验证码输入、不输入、没点击获取验证码
        verify_code = Config.Config.verify_code
        logger = logging.getLogger(__name__)
        yield {
            "driver": driver,
            "element": element,
            "email": email,
            "email_password": email_password,
            "phone": phone,
            "phone_password": phone_password,
            "nick_name": nick_name,
            "verify_code": verify_code,
            "logger": logger
        }
        # 打印yield返回值
        driver.quit()

    # 正常注册流程
    def test_regist_successfull(self, setup):
        data = setup.values()
        print(data)


