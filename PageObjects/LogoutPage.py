# coding=utf-8
from selenium.webdriver.common.by import By
from time import sleep


class LogoutPage(object):
    def __init__(self):
        # 设置
        self.set_up_button = '//span[contains(text(), "设置")]'
        # 退出登陆
        self.logout_button = '//li[contains(text(), "退出登录")]'

    def test_user_logout(self, driver):
        driver.find_element(By.XPATH, self.set_up_button).click()
        sleep(1)
        driver.find_element(By.XPATH, self.logout_button).click()
