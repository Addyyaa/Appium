login_page_tips = {
    "Ch_Phone_Login_PasswdInputTip": '//android.view.View[@content-desc="请填写密码"]',
    "Ch_AgreementTip": '//android.view.View[@content-desc="请阅读并同意用户协议及隐私政策"]',
    "Ch_Phone_Login_CorrectPhoneTip": '//android.view.View[@content-desc="请输入正确的手机号码"]',
    "Ch_PasswdFormatTip": '//android.view.View[@content-desc="密码由字母和数字组成，长度在6-12之间"]',
    "Ch_PasswdErrorTip": '//android.view.View[@content-desc="账号或密码错误"]',
    "Ch_NoSuchUserTip": '//android.view.View[@content-desc="用户信息不存在，请确保用户信息及所选区域是否正确"]',
    "Ch_Email_Login_EmailInputTip": '//android.view.View[@content-desc="请输入邮箱账号"]',
    "Ch_Email_Login_PasswdInputTip": '//android.view.View[@content-desc="请填写密码"]',
    "Ch_Email_Login_CorrectEmailTip": '//android.view.View[@content-desc="请输入正确的邮箱账号"]',
    "Ch_CodeInputTip": '//android.view.View[@content-desc="请输入验证码"]',
    "Ch_sendCodeTip": '//android.view.View[@content-desc="请先获取验证码"]',
    "Ch_CodeErrorTip": '//android.view.View[@content-desc="验证码错误"]',
    # 登陆界面手机号输入提示
    "Ch_Phone_Register_PhoneInputTips": '//android.widget.FrameLayout['
                                        '@resource-id="android:id/content"]/android.widget.FrameLayout/android'
                                        '.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout'
                                        '/android.view.ViewGroup'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout['
                                        '2]/android.widget.FrameLayout['
                                        '2]/android.widget.FrameLayout/android.widget.ImageView/child::*[1]',
}

register_page_tips = {
    # 注册界面请输入邮箱提示
    "Ch_Email_Register_EmailInputTips": '//android.webkit.WebView[@text="pages/mine/reg/index['
                                        '4]"]/android.view.View[1]/android.view.View/android.view.View/android.view'
                                        '.View/child::*[1]',
    "Ch_Email_Register_NickNameInputTips": '//android.widget.TextView[@text="请填写昵称"]',
    "Ch_Email_Register_PasswdInputTips": '//android.widget.TextView[@text="请填写密码"]',
    "Ch_Email_Register_ConfirmPasswdInputTips": '//android.widget.TextView[@text="请再次填写密码"]',
    "Ch_Email_Register_passwdInconsistent": '//android.widget.TextView[@text="密码与确认密码不一致"]',
    "Ch_PasswdFormatTip": '//android.widget.TextView[@text="密码由字母和数字组成，长度在6-12之间"]',
    "Ch_sendCode": '//android.widget.TextView[@text="请先获取验证码"]',
    "Ch_CodeInput": '//android.widget.TextView[@text="请输入验证码"]',
    "Ch_AgreementTip": '//android.widget.TextView[@text="请先阅读并勾选同意用户协议和隐私协议"]',
    "Ch_codeError": '//android.widget.TextView[@text="验证码错误"]',
    "Ch_Email_Register_CorrectEmailTip": '//android.widget.TextView[@text="请输入正确的邮箱账号"]',
    "Ch_Phone_Register_CorrectPhoneTip": '//android.widget.TextView[@text="请输入正确的手机号码"]',
    "Ch_UserExist": '//android.widget.TextView[@text="手机号或邮箱已存在"]',
}
