# coding=utf-8
from selenium.webdriver.common.by import By
from time import sleep


class DispatchingManagementPage(object):
    # 第一个派单button
    first_dispatch_button = (By.XPATH, "//button[contains(text(), '派单')]")
    # 1-抢修button 2-试验button 3-维修button 4-巡检button
    select_work_order_type_button = (By.XPATH, "//input[@name='chosePeo'and@data-type='3']")
    # 请选择派发流程button
    dispatch_flow_button = (By.XPATH, "//span[contains(text(), '请选择派发流程')]/following-sibling::div[1]/div[1]/div[1]/input[2]")
    # 选择抢修工作流button
    select_dispatch_flow = (By.XPATH, "//li[contains(text(), '抢修工作流')]")
    # 负责人按钮
    leader_button = (By.XPATH, "//span[contains(text(), '负责人')]/following-sibling::div[1]/div[1]/div[1]/input[2]")
    # 负责人选项
    leader_select_button = (By.XPATH, '//*[@id="sendOrder"]/div[2]/div[2]/div[3]/div[3]/div/div/div[2]/ul[2]/li[2]')
    # 自动匹配button
    auto_match_button = (By.CLASS_NAME, 'automatch')
    # 选择第一个人员checkbox
    first_user_list = (By.XPATH, '//*[@id="sendOrder"]/div[3]/div/div[1]/div[1]/div[2]')
    # 自动匹配界面确定button
    confirm_button = (By.CLASS_NAME, 'automatchPopConfirm')
    # 工单内容描述input
    work_order_content = (By.XPATH, "//span[contains(text(), '工单内容描述')]/following-sibling::div[1]/div/textarea")
    # 计划开始时间input
    plan_start_time_js = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
    plan_start_time_input = (By.XPATH, '//*[@id="sendOrder"]/div[2]/div[2]/div[3]/div[8]/div/div/div[1]/div/input')
    # 计划时间确定button
    plan_confirm_button1 = (By.XPATH, '//span[contains(text(), "确定")]')
    plan_confirm_button2 = (By.XPATH, '//span[contains(text(), "确定")]')
    # 计划结束时间input
    plan_end_time_js = 'document.getElementsByTagName("input")[15].removeAttribute("readonly");'
    plan_end_time_input = (By.XPATH, '//*[@id="sendOrder"]/div[2]/div[2]/div[3]/div[9]/div/div/div[1]/div/input')
    # 班组input
    team_group_input = (By.XPATH, '//span[contains(text(), "班组")]/following-sibling::div[1]/div/input')
    # 派单button
    dispatch_button = (By.XPATH, '//button[contains(text(), "派单")]')

    def click_first_dispatch_button(self, driver):
        driver.find_element(*self.first_dispatch_button).click()

    def click_slow_repair_button(self, driver):
        driver.find_element(*self.select_work_order_type_button).click()

    def click_dispatch_flow_button(self, driver):
        driver.find_element(*self.dispatch_flow_button).click()

    def select_first_dispatch_flow(self, driver):
        driver.find_element(*self.select_dispatch_flow).click()

    def click_auto_match_button(self, driver):
        driver.find_element(*self.auto_match_button).click()

    def click_auto_match_first_user_list(self, driver):
        driver.find_element(*self.first_user_list).click()

    def click_auto_match_confirm_button(self, driver):
        driver.find_element(*self.confirm_button).click()

    def input_work_order_content(self, driver, work_order_content_input):
        driver.find_element(*self.work_order_content).send_keys(work_order_content_input)

    def select_plan_start_time(self, driver, plan_start_time):
        driver.execute_script(self.plan_start_time_js)
        sleep(1)
        driver.find_element(*self.plan_start_time_input).send_keys(plan_start_time)
        sleep(1)
        driver.find_elements(*self.plan_confirm_button1)[0].click()

    def select_plan_end_time(self, driver, plan_end_time):
        driver.execute_script(self.plan_end_time_js)
        sleep(1)
        driver.find_element(*self.plan_end_time_input).send_keys(plan_end_time)
        sleep(1)
        driver.find_elements(*self.plan_confirm_button2)[1].click()

    def input_team_group(self, driver, team_group):
        driver.find_element(*self.team_group_input).send_keys(team_group)

    def click_dispatch_button(self, driver):
        driver.find_element(*self.dispatch_button).click()

    def click_leader_button(self, driver):
        driver.find_element(*self.leader_button).click()

    def click_leader_select_button(self, driver):
        driver.find_element(*self.leader_select_button).click()
