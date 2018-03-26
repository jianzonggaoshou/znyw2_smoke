# coding=utf-8
from selenium.webdriver.common.by import By


class HomePage(object):
    def __init__(self):
        self.real_time_monitoring_button = "//a[contains(text(), '实时监控')]"
        self.dispatching_management_button = "//a[contains(text(), '调度管理')]"
        self.work_order_button = "//a[contains(text(), '工单')]"

    def click_real_time_monitoring(self, driver):
        driver.find_element(By.XPATH, self.real_time_monitoring_button).click()

    def click_dispatching_management(self, driver):
        driver.find_element(By.XPATH, self.dispatching_management_button).click()

    def click_work_order(self, driver):
        driver.find_element(By.XPATH, self.work_order_button).click()
