# coding=utf-8
from selenium.webdriver.common.by import By
from time import sleep


class LogoutPage(object):
    # 设置button
    set_up_button = (By.XPATH, '//span[contains(text(), "设置")]')
    # 退出登录button
    logout_button = (By.XPATH, '//li[contains(text(), "退出登录")]')

    def test_user_logout(self, driver):
        driver.find_element(*self.set_up_button).click()
        sleep(1)
        driver.find_element(*self.logout_button).click()
