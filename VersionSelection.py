from Element import Element_version
class VersionSelection:
    # 元素实例
    element = Element_version()
    def __init__(self, driver):
        self.driver = driver
    def version_selection(self, version="Chinese", language="Chinese"):
        self.driver.implicitly_wait(10)
        judege = self.driver.find_element(by='id', value=self.element.judege)
        print(judege.text)
        if judege.text == "同意并接受":
            print('判断通过')
            judege.click()
            self.driver.implicitly_wait(15)
            self.driver.find_element(by='xpath', value=self.element.area1).click()
            if version == "Chinese" and language == "Chinese":
                self.driver.find_element(by='xpath', value=self.element.Ch_China).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Language).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Chinese).click()
                self.driver.implicitly_wait(10)
                print("版本选择完毕点击确认")
                self.driver.find_element(by='xpath', value=self.element.Ch_Confirm).click()
            elif version == "Chinese" and language == "English":
                self.driver.find_element(by='xpath', value=self.element.Ch_China).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Language).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_English).click()
                self.driver.implicitly_wait(10)
                # 点击确认
                print("版本选择完毕点击确认")
                self.driver.find_element(by='xpath', value=self.element.En_Confirm).click()
            elif version == "English" and language == "Chinese":
                self.driver.find_element(by='xpath', value=self.element.Ch_USA).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Language).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Chinese).click()
                self.driver.implicitly_wait(10)
                print("版本选择完毕点击确认")
                self.driver.find_element(by='xpath', value=self.element.Ch_Confirm).click()
            elif version == "English" and language == "English":
                self.driver.find_element(by='xpath', value=self.element.Ch_USA).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_Language).click()
                self.driver.find_element(by='xpath', value=self.element.Ch_English).click()
                self.driver.implicitly_wait(10)
                print("版本选择完毕点击确认")
                self.driver.find_element(by='xpath', value=self.element.En_Confirm).click()
            else:
                print("error")
            print("开始识别中英文版本")
        elif judege.text == "ACCEPT":
            print("已识别为英文")
            judege.click()
            print("已点击接受")
            self.driver.implicitly_wait(10)
            # 弹出地域选项
            self.driver.find_element(by='xpath', value=self.element.area2).click()
            print("弹出地域选项")
            if version == "Chinese" and language == "Chinese":
                print("输入地域中国、语言中文")
                # 选择中国
                self.driver.find_element(by='xpath',
                                         value=self.element.En_China).click()
                print("地域选择China")
                # 弹出语言选项框
                self.driver.find_element(by='xpath', value=self.element.En_Language).click()
                # 选择中文
                self.driver.find_element(by='xpath',
                                         value=self.element.En_Chinese).click()
                print("语言选择中文")
                self.driver.implicitly_wait(10)
                # 点击确认
                self.driver.find_element(by='xpath', value=self.element.Ch_Confirm).click()
            elif version == "Chinese" and language == "English":
                print("输入地域中国、语言英文")
                # 选择中国
                self.driver.find_element(by='xpath', value=self.element.En_China).click()
                print("地域选择China")
                # 弹出语言选项框
                self.driver.find_element(by ='xpath', value=self.element.En_Language).click()
                self.driver.implicitly_wait(10)
                # 选择英文
                self.driver.find_element(by='xpath', value=self.element.En_English).click()
                print("语言选择英文")
                self.driver.implicitly_wait(10)
                # 点击确认
                self.driver.find_element(by='xpath', value=self.element.En_Confirm).click()
            elif version == "English" and language == "Chinese":
                print("输入地域美国、语言中文")
                # 选择美国
                self.driver.find_element(by='xpath', value=self.element.En_USA).click()
                print("地域选择USA")
                # 弹出语言选项框
                self.driver.find_element(by='xpath', value=self.element.En_Language).click()
                # 选择中文
                self.driver.find_element(by='xpath', value=self.element.En_Chinese).click()
                print("语言选择中文")
                self.driver.implicitly_wait(10)
                # 点击确认
                self.driver.find_element(by='xpath', value=self.element.Ch_Confirm).click()
            elif version == "English" and language == "English":
                print("输入地域美国、语言英文")
                # 选择美国
                self.driver.find_element(by='xpath', value=self.element.En_USA).click()
                print("地域选择USA")
                # 弹出语言选项框
                self.driver.find_element(by='xpath', value=self.element.En_Language).click()
                # 选择英文
                self.driver.find_element(by='xpath', value=self.element.En_English).click()
                print("语言选择英文")
                self.driver.implicitly_wait(10)
                # 点击确认
                self.driver.find_element(by='xpath', value=self.element.En_Confirm).click()
            else:
                print("error")
                self.driver.implicitly_wait(10)
        else:
            print("error")
