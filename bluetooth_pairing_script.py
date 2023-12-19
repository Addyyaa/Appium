import os

import LoginPage
from Init import get_driver
from VersionSelection import VersionSelection
from LoginPage import LoginPage
import Config
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from time import sleep
import time
import sys


class bluetooth_pairing_test:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s - %(exc_info)s')
        language = 'Chinese'
        versions = 'Chinese'
        agreement_verifycode = (True, True)
        getCode_fillCode = (True, None)
        login_type = "phone"
        self.driver = get_driver()
        version = VersionSelection(self.driver)
        version.version_selection(version=versions, language=language)
        Config.Config.phone = "15250996938"
        login = LoginPage(self.driver)
        self.logger = logging.getLogger(__name__)
        if agreement_verifycode[0]:
            login.login(getCode_fillCode, login_type, language, agreement_verifycode, )
        elif not agreement_verifycode[0]:
            login.login(login_type, language)
        else:
            print("Agreement 变量错误！")

    def screenshot(self, name):
        save_directory = "fail_screenshot"
        os.makedirs(save_directory, exist_ok=True)
        # 构造文件路径
        file_path = os.path.join(save_directory, name)
        screenshot_data = self.driver.get_screenshot_as_png()
        with open(file_path, 'wb') as f:
            f.write(screenshot_data)

    def detect_network_setup_interface(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        try:
            add_device = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, '//android.webkit.WebView[@text="pages/index['
                                                            '2]"]/android.view.View[2]/android.widget.TextView[1]'))
            )
            add_device.click()
        except selenium.common.exceptions.TimeoutException:
            self.logger.error("未找到添加设备按钮")

        try:
            product_selector = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, '//android.webkit.WebView[@text="pages/work/addAhost1['
                                                            '4]"]/android.view.View[3]'))
            )
            product_selector.click()
        except selenium.common.exceptions.TimeoutException:
            self.logger.error("未找到产品选择按钮")

        try:
            location_permission = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, '//android.widget.Button[@text="仅在使用中允许"]'))
            )
            location_permission.click()
        except selenium.common.exceptions.TimeoutException:
            self.logger.error("未找到位置授权按钮")

        try:
            location_permission = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, '//android.widget.Button[@text="始终允许"]'))
            )
            location_permission.click()
        except selenium.common.exceptions.TimeoutException:
            self.logger.error("未找到蓝牙授权按钮")

        sleep(5)

        count = 0
        one_time_setup_successful = 0
        circle_times = 100
        devices_num = 4
        encoding = 'utf-8'
        for i in range(circle_times):
            devices_successful = 0
            device1 = "Pintura-blt-L000892"
            device2 = "Pintura-blt-Ltest20"
            device3 = "Pintura-blt-L000308"
            device4 = "Pintura-blt-L000329"
            wifi_name = "zhancheng"
            wifi_passwd = "nanjingzhancheng"
            device1_element, device2_element, device3_element, device4_element = False, False, False, False
            device1_result, device2_result, device3_result, device4_result = None, None, None, None
            try:
                device1_element = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, f'//android.widget.TextView['
                                                                f'@resource-id="com.ost.pintura:id/tv_name" and '
                                                                f'@text="{device1}"]'))
                )
                device1_element.click()
                wait.until((ec.staleness_of(device1_element)))
                self.logger.info(f"找到设备：{device1}")
            except selenium.common.exceptions.TimeoutException:
                self.logger.error(f"未找到设备：{device1}")

            try:
                device2_element = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, f'//android.widget.TextView['
                                                                '@resource-id="com.ost.pintura:id/tv_name" and '
                                                                f'@text="{device2}"]'))
                )
                device2_element.click()
                wait.until((ec.staleness_of(device2_element)))
                self.logger.info(f"找到设备：{device2}")
            except selenium.common.exceptions.TimeoutException:
                self.logger.error(f"未找到设备：{device2}")

            try:
                device3_element = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, f'//android.widget.TextView['
                                                                '@resource-id="com.ost.pintura:id/tv_name" and '
                                                                f'@text="{device3}"]'))
                )
                device3_element.click()
                wait.until((ec.staleness_of(device3_element)))
                self.logger.info(f"找到设备：{device3}")
            except selenium.common.exceptions.TimeoutException:
                self.logger.error(f"未找到设备：{device3}")

            try:
                device4_element = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, f'//android.widget.TextView['
                                                                '@resource-id="com.ost.pintura:id/tv_name" and '
                                                                f'@text="{device4}"]'))
                )
                device4_element.click()
                self.logger.info(f"找到设备：{device4}")
            except selenium.common.exceptions.TimeoutException:
                self.logger.error(f"未找到设备：{device4}")
            if not (device1_element and device2_element and device3_element and device4_element):
                self.logger.error("即将退出程序")
                break

            start_setup_button = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.ID, 'com.ost.pintura:id/btn_next'))
            )
            start_setup_button.click()
            # 等待页面加载完成
            try:
                result = WebDriverWait(driver, 15).until(
                    ec.invisibility_of_element_located((By.CLASS_NAME, 'android.widget.ImageView'))
                )
            except selenium.common.exceptions.TimeoutException:
                self.logger.error("未找到页面刷新元素标记")
                break
            if result:
                self.logger.info("页面刷新完成")
                try:
                    wifi_list = WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located((By.XPATH,
                                                          '//android.view.ViewGroup[@resource-id="com.ost.pintura:id/swipe_layout"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.View[2]'))
                    )
                    wifi_list.click()
                    driver.implicitly_wait(1)
                except selenium.common.exceptions.TimeoutException:
                    self.logger.error("未找到wifi列表")

            # 选择WiFi
            try:
                wifi = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, f'//android.widget.TextView[@text="{wifi_name}"]'))
                )
                wifi.click()
                self.logger.info(f"已选择WiFi：{wifi_name}")
            except selenium.common.exceptions.TimeoutException:
                self.logger.error(f"未找到wifi：{wifi_name}")

            try:
                wifi_passwd_element = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.ID, 'com.ost.pintura:id/et_pwd'))
                )
                wifi_passwd_element.send_keys(wifi_passwd)
                self.logger.info(f"已输入密码：{wifi_passwd}")
            except selenium.common.exceptions.TimeoutException:
                self.logger.error(f"未找到密码输入框")
            try:
                connect_button = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.ID, 'com.ost.pintura:id/btn_ok'))
                )
                connect_button.click()
                self.logger.info(f"开始配网..............")
            except selenium.common.exceptions.TimeoutException:
                self.logger.error(f"未找到连接按钮")
            # 记录开始时间
            start_time = time.time()

            # 等待配网成功
            try:
                device1_complete = WebDriverWait(driver, 60).until(
                    ec.any_of(
                        ec.text_to_be_present_in_element(
                            (By.XPATH, f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and '
                                       f'@text="{device1}"]/following-sibling::*[1]'), "配网成功"
                        ),
                        ec.text_to_be_present_in_element(
                            (By.XPATH, f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and '
                                       f'@text="{device1}"]/following-sibling::*[1]'), "连接失败"
                        )
                    )
                )
                device2_complete = WebDriverWait(driver, 60).until(
                    ec.any_of(
                        ec.text_to_be_present_in_element(
                            (By.XPATH, f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and '
                                       f'@text="{device2}"]/following-sibling::*[1]'), "配网成功"
                        ),
                        ec.text_to_be_present_in_element(
                            (By.XPATH, f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and '
                                       f'@text="{device2}"]/following-sibling::*[1]'), "连接失败"
                        )
                    )
                )

                device3_complete = WebDriverWait(driver, 60).until(
                    ec.any_of(
                        ec.text_to_be_present_in_element(
                            (By.XPATH, f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and '
                                       f'@text="{device3}"]/following-sibling::*[1]'), "配网成功"
                        ),
                        ec.text_to_be_present_in_element(
                            (By.XPATH, f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and '
                                       f'@text="{device3}"]/following-sibling::*[1]'), "连接失败"
                        )
                    )
                )
                device4_complete = WebDriverWait(driver, 60).until(
                    ec.any_of(
                        ec.text_to_be_present_in_element(
                            (By.XPATH, f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and '
                                       f'@text="{device4}"]/following-sibling::*[1]'), "配网成功"
                        ),
                        ec.text_to_be_present_in_element(
                            (By.XPATH, f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and '
                                       f'@text="{device4}"]/following-sibling::*[1]'), "连接失败"
                        )
                    )
                )
            except selenium.common.exceptions.TimeoutException:
                self.logger.error("配网超时")
                break
            # 统计配网成功数量以及四台设备配网所需完成实际时间
            if device1_complete and device2_complete and device3_complete and device4_complete:
                end_time = time.time()
                # 总用时
                total_time = round(end_time - start_time, 2)
                self.logger.info(f"总用时：{total_time}s")
                # 重新获取元素
                device1_complete = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH,
                                                      f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and @text="{device1}"]/following-sibling::*[1]'))
                )
                device2_complete = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH,
                                                      f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and @text="{device2}"]/following-sibling::*[1]'))
                )
                device3_complete = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH,
                                                      f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and @text="{device3}"]/following-sibling::*[1]'))
                )
                device4_complete = WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH,
                                                      f'//android.widget.TextView[@resource-id="com.ost.pintura:id/tv_name" and @text="{device4}"]/following-sibling::*[1]'))
                )
                device1_result = device1_complete.text
                self.logger.info(device1_result)
                device2_result = device2_complete.text
                self.logger.info(device2_result)
                device3_result = device3_complete.text
                self.logger.info(device3_result)
                device4_result = device4_complete.text
                self.logger.info(device4_result)
                device_results = [device1_result, device2_result, device3_result, device4_result]
                for result in device_results:
                    if result == "配网成功":
                        devices_successful += 1
                if device1_result == device2_result == device3_result == device4_result == "配网成功":
                    one_time_setup_successful += 1
                self.logger.info(
                    f"配网成功的设备数量：{devices_successful}，失败的设备数量：{devices_num - devices_successful}")
                count += 1
                # 生成配网结果文件
                with open("配网结果.txt", "a", encoding=encoding) as f:
                    f.write(f"第{count}次配网：{device1}-{device1_result}\t{device2}-{device2_result}\t{device3}-{device3_result}\t{device4}-{device4_result}\n")
                # 返回产品选择界面
                driver.press_keycode(4)
                driver.press_keycode(4)
                driver.press_keycode(4)
                try:
                    product_selector = WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located((By.XPATH,

                                                          '//android.webkit.WebView[@text="pages/work/addAhost1[4]"]/android.view.View[3]'))
                    )
                    product_selector.click()
                except selenium.common.exceptions.TimeoutException:
                    self.logger.error("未找到产品选择按钮")
            # 如果存在配网失败的设备，则截图
            if device1_result == "配网失败" or device2_result == "配网失败" or device3_result == "配网失败" or device4_result == "配网失败":
                self.logger.info("发现配网失败的设备，将进行截图")
                driver.screenshot(f"第{count}次配网失败.png")

        # 统计总的成功率
        total_successful_rate = round(one_time_setup_successful / count * 100, 2)
        self.logger.info(
            f"总计配网:{count}次，成功:{one_time_setup_successful}次，失败:{count - one_time_setup_successful}次")
        self.logger.info(f"总的成功率:{total_successful_rate}%")
        with open("配网结果.txt", "a", encoding=encoding) as f:
            f.write(f"总的成功率:{total_successful_rate}%\n")
        if count != circle_times:
            self.logger.info(f"由于异常原因导致还差{circle_times - count}次配网，程序即将退出")
            sys.exit()

te = bluetooth_pairing_test()
te.detect_network_setup_interface()
