class Element_version:
    # -------------------------------------------------------------------------------------------------初始界面----------------------------------------------------------------------
    # 版本判断元素
    judege = 'com.ost.pintura:id/btn_custom_privacy_sure'
    # 中文版同意协议
    agree1 = '//android.widget.Button[@resource-id="com.ost.pintura:id/btn_custom_privacy_sure"]'
    # 英文版同意协议
    agree2 = '//android.widget.Button[@resource-id="com.ost.pintura:id/btn_custom_privacy_sure"]'
    # 中文弹出地域列表
    area1 = '//android.webkit.WebView[@text="pages/area[2]"]/android.view.View[1]'
    # 中文版-地域-中国
    Ch_China = '(//android.widget.TextView[@text="中国大陆"])[2]'
    # 中文版-地域-美国
    Ch_USA = '//android.widget.TextView[@text="美国"]'
    # 英文弹出地域列表
    area2 = '//android.webkit.WebView[@text="pages/area[2]"]/android.view.View[1]/android.view.View'
    # 英文版-地域-中国
    En_China = '//android.widget.TextView[@text="China"]'
    # 英文版-地域-美国
    En_USA = '(//android.widget.TextView[@text="United States"])[2]'
    # 中文版-语言列表
    Ch_Language = '//android.widget.TextView[@text="简体中文"]'
    # 中文版-中文
    Ch_Chinese = '(//android.widget.TextView[@text="简体中文"])[2]'
    # 中文版-English
    Ch_English = '//android.widget.TextView[@text="English"]'
    # 英文版-语言列表
    En_Language = '//android.webkit.WebView[@text="pages/area[2]"]/android.view.View[2]/android.view.View'
    # 英文版-English
    En_English = '(//android.widget.TextView[@text="English"])[2]'
    # 英文版-中文
    En_Chinese = '//android.widget.TextView[@text="简体中文"]'
    # 中文版-确认
    Ch_Confirm = '//android.widget.TextView[@text="确定"]'
    # 英文版-确认
    En_Confirm = '//android.widget.TextView[@text="Confirm"]'
    # ---------------------------------------------------------------------------------------------登录界面-------------------------------------------------------------------
    Ch_UserAgreement = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout' \
                       '/android.widget.FrameLayout/' \
                       'android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget' \
                       '.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ImageView'
    En_UserAgreement = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout' \
                       '/android.widget.FrameLayout/' \
                       'android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget' \
                       '.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ImageView'
    # 中文版-手机登录
    Ch_Phone_Login = '//android.view.View[@content-desc="手机登录"]'
    # 中文版-邮箱登录
    Ch_Email_Login = '//android.view.View[@content-desc="邮箱登录"]'
    # 中文版-验证码
    Ch_Code_Login = '//android.view.View[@content-desc="验证码登录"]'
    # 中文版-区号
    Ch_Area_List = '//android.view.View[@content-desc=""]'
    # 中文版-区号搜索框
    Ch_Area_Code = '//android.widget.EditText[@text="搜索国家或地区名称"]'
    # 中文版-区号86
    Ch_Area_Code_86 = '//android.view.View[@content-desc="中国大陆(CN)"]'
    # 中文版-区号1
    Ch_Area_Code_1 = '//android.view.View[@content-desc="美国(US)"]'
    # 中文版-清空区号搜索框
    Ch_Area_Code_Clear = '//android.view.View[@content-desc=""]'
    # 中文版-手机号输入框
    Ch_PhoneNumber = '//android.widget.EditText[@text="请输入手机号码"]'
    # 中文版-手机号清除按钮
    Ch_PhoneNumber_Clear = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]' \
                           '/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[3]/android.widget.ImageView'
    # 中文版-手机密码输入（需要先点击）
    Ch_Phone_Passswd = '//android.widget.EditText[@text="请填写密码"]'
    # 中文版-密码明文显示
    Ch_Phone_Passswd_Show = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout' \
                            '/android.widget.FrameLayout[3]' \
                            '/android.widget.FrameLayout[1]/android.widget.FrameLayout[' \
                            '2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ImageView'
    # 中文版-密码密文清除按钮
    Ch_Phone_Passswd_Clear = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout' \
                             '/android.widget.FrameLayout[3]' \
                             '/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.ImageView'
    # 中文版-记住密码
    Ch_Remember = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]' \
                  '/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ImageView'
    # 中文版-找回密码
    Ch_Forget_Passwd = '//android.view.View[@content-desc="找回密码"]'
    # 中文版-地域列表
    Ch_Region_List = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]' \
                     '/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]'
    # 中文版- 中国
    Ch_Region_China = '//android.view.View[@content-desc="中国大陆"]'
    # 中文版- 美国
    Ch_Region_USA = '//android.view.View[@content-desc="美国"]'
    # 中文版-地域取消操作
    Ch_Region_Cancel = '//android.view.View[@content-desc="取消"]'
    # 中文版-切换语言
    Ch_LoginPage_Language = '//android.view.View[@content-desc="切换语言"]'
    # 中文版-注册
    Ch_LoginPage_Register = '//android.view.View[@content-desc="没有账号？立即注册"]'
    # 中文版-用户协议
    Ch_LoginPage_UserAgreement = '//android.view.View[@content-desc="《用户协议》"]'
    # 中文版-隐私政策
    Ch_LoginPage_Privacy = '//android.view.View[@content-desc="《隐私政策》"]'
    # 中文版-当前地域
    Ch_Current_Area = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android' \
                      '.widget.FrameLayout[3]/android.widget.FrameLayout[3]/android.widget.FrameLayout[' \
                      '1]/android.widget.FrameLayout/android.widget.FrameLayout/*'
    # 中文版-邮箱账号输入
    Ch_Email_Input = '//android.widget.EditText[@text="请输入邮箱账号"]'
    # 中文版-邮箱账号清除按钮
    Ch_Email_Input_Clear = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]' \
                           '/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView'
    # 中文版-邮箱密码输入
    Ch_Email_Passwd = '//android.widget.EditText[@text="请填写密码"]'
    # 中文版-邮箱密码明文显示
    Ch_Email_PasswdShow = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[1' \
                          '/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ImageView'
    # 中文版-邮箱密码清除按钮
    Ch_Email_PasswdClear = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android' \
                           '.widget.FrameLayout[3]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.ImageView'
    # 中文版-验证码登录手机号输入
    Ch_CodeLogin_Number = '//android.widget.EditText[@text="请输入手机号码"]'
    # 中文版-获取验证码
    Ch_CodeLogin_Get = '//android.view.View[@content-desc="获取验证码"]'
    # 中文版-验证码登录验证码
    Ch_CodeLogin_CodeInput = '//android.widget.EditText[@text="请输入验证码"]'
    # 中文版- 登录按钮
    Ch_LoginButton = '//android.view.View[@content-desc="登录"]'
    # 英文版-手机登录
    En_Phone_Login = '//android.view.View[@content-desc="Phone"]'
    # 英文版-邮箱登录
    En_Email_Login = '//android.view.View[@content-desc="Email"]'
    # 英文版-验证码登录
    En_Code_Login = '//android.view.View[@content-desc="Code"]'
    # 英文版-区号列表
    En_AreCode_List = '//android.view.View[@content-desc=""]'
    # 英文版-区号搜索框
    En_AreCode_Input = '//android.widget.EditText[@text="search by country or region name"]'
    # 英文版-区号86
    En_AreCode_86 = '//android.view.View[@content-desc="China(CN)"]'
    # 英文版-区号1
    En_AreCode_1 = '//android.view.View[@content-desc="United States(US)"]'
    # 英文版-清空区号搜索框
    En_AreCode_Clear = '//android.view.View[@content-desc=""]'
    # 英文版-手机号输入框
    En_PhoneNumber = '//android.widget.EditText[@text="Please enter your phone number"]'
    # 英文版-手机密码输入
    En_Phone_Passswd = '//android.widget.EditText[@text="Please enter your password"]'
    # 英文版-记住密码
    En_Remember = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]' \
                  '/android.widget.FrameLayout/android.widget.ImageView'
    # 英文版-找回密码
    En_Forget_Passwd = '//android.view.View[@content-desc="Forgot Password?"]'
    # 英文版-地域列表
    En_Region_List = '//android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[3]' \
                     '/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout'
    # 英文版- 中国
    En_Region_China = '//android.view.View[@content-desc="China"]'
    # 英文版- 美国
    En_Region_USA = '//android.view.View[@content-desc="United States"]'
    # 英文版-地域取消操作
    En_Region_Cancel = '//android.view.View[@content-desc="Switch Language"]'
    # 英文版-切换语言
    En_LoginPage_Language = '//android.view.View[@content-desc="Language"]'
    # 英文版-注册
    En_LoginPage_Register = '//android.view.View[@content-desc="New User?<Register Here>"]'
    # 英文版-用户协议
    En_LoginPage_UserAgreement = '//android.view.View[@content-desc="《Service Agreement》"]'
    # 英文版-隐私政策
    En_LoginPage_Privacy = '//android.view.View[@content-desc="《Privacy Policy》"]'
    # 英文版-邮箱账号输入
    En_Email_Input = '//android.widget.EditText[@text="Please enter your email"]'
    # 英文版-邮箱密码输入
    En_Email_Passwd = '///android.widget.EditText[@text="Please enter your password"]'
    # 英文版-验证码登录手机号输入
    En_CodeLogin_Number = '//android.widget.EditText[@text="Please enter your phone number"]'
    # 英文版-获取验证码
    En_CodeLogin_GetCode = '//android.view.View[@content-desc="Get verification code"]'
    # 英文版-验证码登录验证码
    En_CodeLogin_Code = '//android.widget.EditText[@text="Please enter the code"]'
    # 英文版- 登录按钮
    En_LoginButton = '//android.view.View[@content-desc="Sign in"]'
    # 英文版-当前地域
    En_China_Region = '//android.view.View[@content-desc="Country:China"]'
    En_United_States_Region = '//android.view.View[@content-desc="Country:United States"]'
    # 中文版-当前地域
    Ch_China_Region = '//android.view.View[@content-desc="地区:中国大陆"]'
    Ch_United_States_Region = '//android.view.View[@content-desc="地区:美国"]'

    # ---------------------------------------------------------------------------------------------注册页面-------------------------------------------------------------------
    Ch_Phone_Register = '//android.widget.TextView[@text="手机号注册"]'
    Ch_Email_Register = '//android.widget.TextView[@text="邮箱注册"]'
    Ch_Phone_Register_AreaCodeList = '//android.widget.TextView[@resource-id="country"]'
    Ch_Phone_Register_AreaCode_Search = '//android.webkit.WebView[@text="pages/mine/reg/index[2]"]/android.view.View[5]/android.view.View/android.view.View/' \
                                        'android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText'
    # 此元素无法通过sendkeys输入，需要通过虚拟键盘
    Ch_Phone_Register_PhoneNumber = '//android.view.View[@resource-id="phoneCode"]/android.view.View/android.widget.EditText'
    Ch_Phone_Register_Nickname = '(//android.view.View[@resource-id="input"])[1]/android.view.View/android.widget.EditText'
    # 密码输入元素输入后元素会消失
    Ch_Phone_Register_Passwd = '(//android.view.View[@resource-id="input"])[2]/android.view.View/child::*[1]'
    # 密码输入后的密码元素
    Ch_Phone_Register_Passwd_AfterInput = '(//android.view.View[@resource-id="input"])[2]/android.view.View/child::*[1]'
    Ch_Phone_Register_ConfirmPasswd = '(//android.view.View[@resource-id="input"])[3]/android.view.View/child::*[2]'
    Ch_Phone_Register_ConfirmPasswd_AfterInput = '(//android.view.View[@resource-id="input"])[3]/android.view.View/child::*[2]'
    Ch_Phone_Register_Region = '//android.webkit.WebView[@text="pages/mine/reg/index[2]"]/android.view.View[8]'
    Ch_Phone_Register_GetCode = '//android.widget.TextView[@text="发送验证码"]'
    # 此元素无法通过sendkeys输入，需要通过虚拟键盘
    Ch_Phone_Register_CodeInput = '(//android.view.View[@resource-id="input"])[4]/android.view.View/android.widget.EditText'
    Ch_Phone_RegisterButton = '//android.widget.TextView[@text="注 册"]'
    Ch_Email_Register_Email = '(//android.view.View[@resource-id="input"])[1]/android.view.View/android.widget.EditText'
    Ch_Email_Register_Nickname = '(//android.view.View[@resource-id="input"])[2]/android.view.View/android.widget.EditText'
    Ch_Email_Register_Passwd = '(//android.view.View[@resource-id="input"])[3]/android.view.View/android.widget.EditText'
    Ch_Email_Register_Passwd_AfterInput = '(//android.view.View[@resource-id="input"])[3]/android.view.View/child::*[1]'
    Ch_Email_Register_ConfirmPasswd = '(//android.view.View[@resource-id="input"])[4]/android.view.View/android.widget.EditText'
    Ch_Email_Register_ConfirmPasswd_AfterInput = '(//android.view.View[@resource-id="input"])[' \
                                                 '4]/android.view.View/child::*[1]'
    Ch_Email_Register_GetCode = '//android.widget.TextView[@text="发送验证码"]'
    Ch_Email_Register_CodeInput = '(//android.view.View[@resource-id="input"])[' \
                                  '5]/android.view.View/android.widget.EditText'
    # 此元素无法通过sendkeys输入，需要通过虚拟键盘
    Ch_Email_RegisterButton = '//android.widget.TextView[@text="注 册"]'


