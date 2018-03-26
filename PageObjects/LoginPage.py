# coding=utf-8
from selenium.webdriver.common.by import By


class LoginPage(object):
    def __init__(self):
        self.username_input = 'userName'
        self.password_input = 'userPwd'
        self.submit_button = 'loginRegister'

    def test_user_login(self, driver, username, password):
        driver.find_element(By.CLASS_NAME, self.username_input).send_keys(username)
        driver.find_element(By.CLASS_NAME, self.password_input).send_keys(password)
        driver.find_element(By.CLASS_NAME, self.submit_button).click()
