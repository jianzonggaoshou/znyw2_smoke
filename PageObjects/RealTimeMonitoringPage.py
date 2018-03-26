# coding=utf-8
from selenium.webdriver.common.by import By


class RealTimeMonitoringPage(object):
    def __init__(self):
        self.first_card = '//*[@id="realTimeSurveillance"]/div[1]/div[3]/div[1]/div[2]/div[1]/p[1]'
        self.notice_dispatcher_button = "//button[contains(text(), '通知调度')]"
        self.notice_dispatcher_input = "informDispatchContent"
        self.notice_dispatcher_input_confirm_button = "//p[contains(text(), '通知调度')]/following-sibling::div[2]/button[2]"

    def click_first_warn_notice_card(self, driver):
        driver.find_element(By.XPATH, self.first_card).click()

    def click_notice_dispatcher_button(self, driver):
        driver.find_element(By.XPATH, self.notice_dispatcher_button).click()

    def input_notice_dispatcher_dialog(self, driver, notice_dispatcher_content):
        driver.find_element(By.CLASS_NAME, self.notice_dispatcher_input).send_keys(notice_dispatcher_content)

    def click_notice_dispatcher_input_confirm_button(self, driver):
        driver.find_element(By.XPATH, self.notice_dispatcher_input_confirm_button).click()
