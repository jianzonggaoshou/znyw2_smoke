# coding=utf-8
from selenium import webdriver
from configuration import URL
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.WorkOrderPage import WorkOrderPage

from time import sleep
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_smoke1(self):
        """smoke1-BS全流程测试-通过场景"""
        # Chrome驱动
        driver = webdriver.Chrome()
        # 浏览器最大化
        driver.maximize_window()
        # 打开网址
        driver.get(URL.url)
        # 等待
        driver.implicitly_wait(20)
        # loginPage实例化
        loginPage1 = LoginPage()
        loginPage1.test_user_login(driver=driver, username='test', password=123456)
        sleep(3)
        # homePage实例化
        homePage1 = HomePage()
        # workOrder实例化
        workOrder1 = WorkOrderPage()

        """test登陆新建工单"""
        homePage1.click_work_order(driver=driver)
        """新增工单"""
        workOrder1.click_add_order(driver=driver)
        """抢修类型"""
        workOrder1.click_qiangxiu_button(driver=driver)
        """请选择派发流程"""
        workOrder1.click_dispatch_flow_select(driver=driver)
        sleep(3)
        """选择第一个派发"""
        workOrder1.click_dispatch_flow_selected_one(driver=driver)
        """填写项目名称"""
        workOrder1.input_project_name(driver=driver, project_name=u'test项目名称')
        """填写项目地点"""
        workOrder1.input_project_place(driver=driver, project_place=u'test项目地点')
        """选择负责人"""
        workOrder1.click_principal_select(driver=driver)
        """选择第一个负责人"""
        workOrder1.click_principal_selected_one(driver=driver)


        sleep(10)
        # 浏览器退出
        driver.quit()

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
