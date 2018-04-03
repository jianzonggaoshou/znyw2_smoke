# coding=utf-8
from selenium import webdriver
from configuration import URL
from PageObjects.LoginPage import LoginPage
from PageObjects.LogoutPage import LogoutPage
from PageObjects.HomePage import HomePage
from PageObjects.RealTimeMonitoringPage import RealTimeMonitoringPage
from PageObjects.DispatchingManagementPage import DispatchingManagementPage
from PageObjects.WorkOrderPage import WorkOrderPage
from time import sleep
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_smoke1(self):
        """smoke1-BS全流程测试-不通过-再次派单场景"""
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

        """test登陆通知调度"""
        # 调用对象loginPage1的login方法
        loginPage1.test_user_login(driver=driver, username='test', password='123456')
        # homePage实例化
        homePage1 = HomePage()
        # 等待
        driver.implicitly_wait(20)
        # 点击实时监控button
        homePage1.click_real_time_monitoring(driver=driver)
        # 实时监控页面实例化
        realTimeMonitoringPage1 = RealTimeMonitoringPage()
        # 等待
        driver.implicitly_wait(20)
        # 点击实时监控的左侧第一个卡片
        realTimeMonitoringPage1.click_first_warn_notice_card(driver=driver)
        driver.implicitly_wait(20)
        # 点击实时监控的右侧通知调度button
        realTimeMonitoringPage1.click_notice_dispatcher_button(driver=driver)
        driver.implicitly_wait(20)
        # 输入通知调度dialog
        realTimeMonitoringPage1.input_notice_dispatcher_dialog(driver=driver, notice_dispatcher_content=u'通知调度')
        # 点击通知调度dialog的确定button
        driver.implicitly_wait(20)
        realTimeMonitoringPage1.click_notice_dispatcher_input_confirm_button(driver=driver)
        sleep(1)
        # 点击调度管理button
        homePage1.click_dispatching_management(driver=driver)
        # 调度管理页面实例化
        dispatchingManagementPage1 = DispatchingManagementPage()
        # 等待
        sleep(3)
        driver.implicitly_wait(20)
        # 第一个调度单派单
        dispatchingManagementPage1.click_first_dispatch_button(driver=driver)
        driver.implicitly_wait(20)
        # 点击工单类型---3.维修单
        dispatchingManagementPage1.click_slow_repair_button(driver=driver)
        driver.implicitly_wait(20)
        # 点击派发流程按钮
        dispatchingManagementPage1.click_dispatch_flow_button(driver=driver)
        driver.implicitly_wait(20)
        # 选择第一个派发流程
        dispatchingManagementPage1.select_first_dispatch_flow(driver=driver)
        driver.implicitly_wait(20)
        # 点击自动匹配
        sleep(1)
        dispatchingManagementPage1.click_auto_match_button(driver=driver)
        driver.implicitly_wait(20)
        # 自动匹配点击第一个人员
        sleep(1)
        dispatchingManagementPage1.click_auto_match_first_user_list(driver=driver)
        driver.implicitly_wait(20)
        # 点击自动匹配对话框的确定按钮
        dispatchingManagementPage1.click_auto_match_confirm_button(driver=driver)
        driver.implicitly_wait(20)
        # 输入工单内容描述
        dispatchingManagementPage1.input_work_order_content(driver=driver, work_order_content_input=u'工单内容描述')
        driver.implicitly_wait(20)
        # 选择计划开始时间
        dispatchingManagementPage1.select_plan_start_time(driver=driver, plan_start_time='2018-03-22 00:00')
        driver.implicitly_wait(20)
        # 选择计划结束时间
        dispatchingManagementPage1.select_plan_end_time(driver=driver, plan_end_time='2018-12-29 00:00')
        driver.implicitly_wait(20)
        # 输入班组
        dispatchingManagementPage1.input_team_group(driver=driver, team_group=u'巡检一班')
        driver.implicitly_wait(20)
        # 调度管理派单界面的派单按钮
        sleep(1)
        dispatchingManagementPage1.click_dispatch_button(driver=driver)
        sleep(3)
        # 退出登陆实例化
        logoutPage1 = LogoutPage()
        # 退出登陆
        logoutPage1.test_user_logout(driver=driver)

        """电工1登陆，走流程，审核和处理"""
        # 电工1登陆
        loginPage1.test_user_login(driver=driver, username='gongxiang1', password='123456')
        # 等待
        driver.implicitly_wait(20)
        # 点击首页工单按钮
        homePage1.click_work_order(driver=driver)
        sleep(1)
        # 工单实例化
        workOrderPage1 = WorkOrderPage()
        # 等待
        driver.implicitly_wait(20)
        # 点击工单中的我的待办
        workOrderPage1.click_my_to_do_button(driver=driver)
        sleep(1)
        driver.implicitly_wait(20)
        # 点击第一个工单的处理按钮
        workOrderPage1.click_first_deal_button(driver=driver)
        driver.implicitly_wait(20)
        # 填写审核表单
        workOrderPage1.input_audit_form(driver=driver, required_equipment=u'所需设备', required_materials=u'所需材料',
                                        repaired_plan=u'所需计划')
        driver.implicitly_wait(20)
        sleep(1)
        # 点击第一个工单的处理按钮
        workOrderPage1.click_first_deal_button(driver=driver)
        # 填写处理表单
        driver.implicitly_wait(20)
        workOrderPage1.input_deal_form(driver=driver, deal_result=u'处理结果')
        sleep(1)
        driver.implicitly_wait(20)
        # 退出登陆
        logoutPage1.test_user_logout(driver=driver)
        sleep(1)
        driver.implicitly_wait(20)

        """test登陆，走流程，验证--通过"""
        # test登陆
        loginPage1.test_user_login(driver=driver, username='test', password='123456')
        sleep(1)
        driver.implicitly_wait(20)
        # 点击导航的工单按钮
        homePage1.click_work_order(driver=driver)
        # 点击工单中的我的待办
        workOrderPage1.click_my_to_do_button(driver=driver)
        sleep(1)
        driver.implicitly_wait(20)
        # 点击第一个工单的处理按钮
        workOrderPage1.click_first_deal_button(driver=driver)
        driver.implicitly_wait(20)
        # 填写验证表单
        workOrderPage1.input_verify_form(driver=driver, result_description=u'结果描述')
        # 验证表单中的通过按钮
        workOrderPage1.click_vertify_form_no_pass_button(driver=driver)
        sleep(1)
        # 弹窗提示点击再次派单按钮
        driver.implicitly_wait(20)
        workOrderPage1.click_hint_again_dispatch_button(driver=driver)
        sleep(1)

        """再次执行派单流程"""
        # 点击工单类型---3.维修单
        dispatchingManagementPage1.click_slow_repair_button(driver=driver)
        driver.implicitly_wait(20)
        # 点击派发流程按钮
        dispatchingManagementPage1.click_dispatch_flow_button(driver=driver)
        driver.implicitly_wait(20)
        # 选择第一个派发流程
        dispatchingManagementPage1.select_first_dispatch_flow(driver=driver)
        driver.implicitly_wait(20)
        # 点击负责人按钮
        sleep(1)
        dispatchingManagementPage1.click_leader_button(driver=driver)
        driver.implicitly_wait(20)
        # 点击第2个人员
        sleep(1)
        dispatchingManagementPage1.click_leader_select_button(driver=driver)
        driver.implicitly_wait(20)
        # 输入工单内容描述
        dispatchingManagementPage1.input_work_order_content(driver=driver, work_order_content_input=u'工单内容描述')
        driver.implicitly_wait(20)
        # 选择计划开始时间
        dispatchingManagementPage1.select_plan_start_time(driver=driver, plan_start_time='2018-03-22 00:00')
        driver.implicitly_wait(20)
        # 选择计划结束时间
        dispatchingManagementPage1.select_plan_end_time(driver=driver, plan_end_time='2018-12-29 00:00')
        driver.implicitly_wait(20)
        # 输入班组
        dispatchingManagementPage1.input_team_group(driver=driver, team_group=u'巡检一班')
        driver.implicitly_wait(20)
        # 调度管理派单界面的派单按钮
        sleep(1)
        dispatchingManagementPage1.click_dispatch_button(driver=driver)
        sleep(1)
        # 退出登陆实例化
        logoutPage1 = LogoutPage()
        # 退出登陆
        logoutPage1.test_user_logout(driver=driver)

        """电工1登陆，走流程，审核和处理"""
        # 电工1登陆
        loginPage1.test_user_login(driver=driver, username='gongxiang1', password='123456')
        # 等待
        driver.implicitly_wait(20)
        # 点击首页工单按钮
        homePage1.click_work_order(driver=driver)
        sleep(1)
        # 工单实例化
        workOrderPage1 = WorkOrderPage()
        # 等待
        driver.implicitly_wait(20)
        # 点击工单中的我的待办
        workOrderPage1.click_my_to_do_button(driver=driver)
        sleep(1)
        driver.implicitly_wait(20)
        # 点击第一个工单的处理按钮
        workOrderPage1.click_first_deal_button(driver=driver)
        driver.implicitly_wait(20)
        # 填写审核表单
        workOrderPage1.input_audit_form(driver=driver, required_equipment=u'所需设备', required_materials=u'所需材料',
                                        repaired_plan=u'所需计划')
        driver.implicitly_wait(20)
        sleep(1)
        # 点击第一个工单的处理按钮
        workOrderPage1.click_first_deal_button(driver=driver)
        # 填写处理表单
        driver.implicitly_wait(20)
        workOrderPage1.input_deal_form(driver=driver, deal_result=u'处理结果')
        sleep(1)
        driver.implicitly_wait(20)
        # 退出登陆
        logoutPage1.test_user_logout(driver=driver)
        sleep(1)
        driver.implicitly_wait(20)
        sleep(1)

        """test登陆，走流程，验证--通过"""
        # test登陆
        loginPage1.test_user_login(driver=driver, username='test', password='123456')
        sleep(1)
        driver.implicitly_wait(20)
        # 点击导航的工单按钮
        homePage1.click_work_order(driver=driver)
        # 点击工单中的我的待办
        workOrderPage1.click_my_to_do_button(driver=driver)
        sleep(1)
        driver.implicitly_wait(20)
        # 点击第一个工单的处理按钮
        workOrderPage1.click_first_deal_button(driver=driver)
        driver.implicitly_wait(20)
        # 填写验证表单
        workOrderPage1.input_verify_form(driver=driver, result_description=u'结果描述')
        # 验证表单中的通过按钮
        workOrderPage1.click_vertify_form_pass_button(driver=driver)
        sleep(1)

        # 浏览器退出
        driver.quit()

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
