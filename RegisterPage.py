import Init
import Element
import Config
class:
    def __init__(self, driver):
        # TODO 将driver变为传递进来的参数
        self.driver = Init.get_driver()
        self.element = Element.Element_version
        # 账号及密码
        self.email = Config.Config.email
        self.email_password = Config.Config.email_password
        self.phone = Config.Config.phone
        self.phone_password = Config.Config.phone_password
        self.nick_name = Config.Config.nick_name
        # TODO 需要对验证码重新设计，验证码输入、不输入、没点击获取验证码
        self.verify_code = Config.Config.verify_code

    def register(self, register_type="email", language=None, *agreement):
        register_methods = {
            "email": self.register_email,
            "phone": self.register_phone,
        }
        register_method = register_methods.get(register_type)
        if register_method:
            register_method(language, *agreement)
        else:
            print("Invalid register type")

    def register_email(self, language, *agreement):
        if  language == "English":
            print("识别到当前语言为英文")
            print("点击邮箱登录")
            self.driver.find_element(by='xpath', value=self.element.En_Email_Login).click()
            print("进入注册页面")
            self.driver.find_element(by='xpath', value=self.element.En_LoginPage_Register).click()
            self.driver.implicitly_wait(1)
            print("输入邮箱地址")
            self.driver.find_element(by='xpath', value=self.element.En_Email_Input).send_keys(self.email)


