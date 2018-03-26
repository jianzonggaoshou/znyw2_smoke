# coding=utf-8
from selenium.webdriver.common.by import By
from time import sleep


class DispatchingManagementPage(object):
    def __init__(self):
        self.first_dispatch_button = "//button[contains(text(), '派单')]"
        # 1-抢修 2-试验 3-维修 4-巡检
        self.select_work_order_type_button = "//input[@name='chosePeo'and@data-type='3']"
        # 请选择派发流程
        self.dispatch_flow_button = "//span[contains(text(), '请选择派发流程')]/following-sibling::div[1]/div[1]/div[1]/input[2]"
        # 选择抢修工作流
        self.select_dispatch_flow = "//li[contains(text(), '抢修工作流')]"
        # 自动匹配
        self.auto_match_button = 'automatch'
        # 选择第一个人员
        self.first_user_list = '//*[@id="sendOrder"]/div[3]/div/div[1]/div[1]/div[2]'
        # 确定按钮
        self.confirm_button = 'automatchPopConfirm'
        # 工单内容描述
        self.work_order_content = "//span[contains(text(), '工单内容描述')]/following-sibling::div[1]/div/textarea"
        # 计划开始时间
        self.plan_start_time_js = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'
        self.plan_start_time_input = '//*[@id="sendOrder"]/div[2]/div[2]/div[3]/div[8]/div/div/div[1]/div/input'
        # 计划时间确定按钮
        self.plan_confirm_button1 = '//span[contains(text(), "确定")]'
        self.plan_confirm_button2 = '//span[contains(text(), "确定")]'
        # 计划结束时间
        self.plan_end_time_js = 'document.getElementsByTagName("input")[15].removeAttribute("readonly");'
        self.plan_end_time_input = '//*[@id="sendOrder"]/div[2]/div[2]/div[3]/div[9]/div/div/div[1]/div/input'
        # 班组
        self.team_group_input = '//span[contains(text(), "班组")]/following-sibling::div[1]/div/input'
        # 派单
        self.dispatch_button = '//button[contains(text(), "派单")]'

    def click_first_dispatch_button(self, driver):
        driver.find_element(By.XPATH, self.first_dispatch_button).click()

    def click_slow_repair_button(self, driver):
        driver.find_element(By.XPATH, self.select_work_order_type_button).click()

    def click_dispatch_flow_button(self, driver):
        driver.find_element(By.XPATH, self.dispatch_flow_button).click()

    def select_first_dispatch_flow(self, driver):
        driver.find_element(By.XPATH, self.select_dispatch_flow).click()

    def click_auto_match_button(self, driver):
        driver.find_element(By.CLASS_NAME, self.auto_match_button).click()

    def click_auto_match_first_user_list(self, driver):
        driver.find_element(By.XPATH, self.first_user_list).click()

    def click_auto_match_confirm_button(self, driver):
        driver.find_element(By.CLASS_NAME, self.confirm_button).click()

    def input_work_order_content(self, driver, work_order_content_input):
        driver.find_element(By.XPATH, self.work_order_content).send_keys(work_order_content_input)

    def select_plan_start_time(self, driver, plan_start_time):
        driver.execute_script(self.plan_start_time_js)
        sleep(1)
        driver.find_element(By.XPATH, self.plan_start_time_input).send_keys(plan_start_time)
        sleep(1)
        driver.find_elements(By.XPATH, self.plan_confirm_button1)[0].click()

    def select_plan_end_time(self, driver, plan_end_time):
        driver.execute_script(self.plan_end_time_js)
        sleep(1)
        driver.find_element(By.XPATH, self.plan_end_time_input).send_keys(plan_end_time)
        sleep(1)
        driver.find_elements(By.XPATH, self.plan_confirm_button2)[1].click()

    def input_team_group(self, driver, team_group):
        driver.find_element(By.XPATH, self.team_group_input).send_keys(team_group)

    def click_dispatch_button(self, driver):
        driver.find_element(By.XPATH, self.dispatch_button).click()
