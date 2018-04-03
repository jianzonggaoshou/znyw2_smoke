# coding=utf-8
from selenium.webdriver.common.by import By


class LoginPage(object):
    # 账号input
    username_input = (By.CLASS_NAME, 'userName')
    # 密码input
    password_input = (By.CLASS_NAME, 'userPwd')
    # 登录button
    submit_button = (By.CLASS_NAME, 'loginRegister')

    def test_user_login(self, driver, username, password):
        driver.find_element(*self.username_input).send_keys(username)
        driver.find_element(*self.password_input).send_keys(password)
        driver.find_element(*self.submit_button).click()
