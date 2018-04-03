# coding=utf-8
from selenium.webdriver.common.by import By


class RealTimeMonitoringPage(object):
    # 左侧第一个卡片div
    first_card = (By.XPATH, '//*[@id="realTimeSurveillance"]/div[1]/div[3]/div[1]/div[2]/div[1]/p[1]')
    # 右侧通知调度button
    notice_dispatcher_button = (By.XPATH, "//button[contains(text(), '通知调度')]")
    # 通知调度弹窗输入input
    notice_dispatcher_input = (By.CLASS_NAME, "informDispatchContent")
    # 通知调度弹窗确认button
    notice_dispatcher_input_confirm_button = (By.XPATH, "//p[contains(text(), '通知调度')]/following-sibling::div[2]/button[2]")

    def click_first_warn_notice_card(self, driver):
        driver.find_element(*self.first_card).click()

    def click_notice_dispatcher_button(self, driver):
        driver.find_element(*self.notice_dispatcher_button).click()

    def input_notice_dispatcher_dialog(self, driver, notice_dispatcher_content):
        driver.find_element(*self.notice_dispatcher_input).send_keys(notice_dispatcher_content)

    def click_notice_dispatcher_input_confirm_button(self, driver):
        driver.find_element(*self.notice_dispatcher_input_confirm_button).click()
