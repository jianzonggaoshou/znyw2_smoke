# coding=utf-8
from selenium.webdriver.common.by import By


class HomePage(object):
    # 导航栏-实时监控button
    real_time_monitoring_button = (By.XPATH, "//a[contains(text(), '实时监控')]")
    # 导航栏-调度管理button
    dispatching_management_button = (By.XPATH, "//a[contains(text(), '调度管理')]")
    # 导航栏-工单button
    work_order_button = (By.XPATH, "//a[contains(text(), '工单')]")

    def click_real_time_monitoring(self, driver):
        driver.find_element(*self.real_time_monitoring_button).click()

    def click_dispatching_management(self, driver):
        driver.find_element(*self.dispatching_management_button).click()

    def click_work_order(self, driver):
        driver.find_element(*self.work_order_button).click()
