# coding=utf-8
from selenium.webdriver.common.by import By


class WorkOrderPage(object):
    # 新增工单
    add_order_button = (By.XPATH, "//a[contains(text(), '新增工单')]")
    # 抢修button
    qiangxiu_button = (By.XPATH, "//input[@type='radio' and @data-type='1']")
    # 试验button
    shiyan_button = (By.XPATH, "//input[@type='radio' and @data-type='2']")
    # 维修button
    weixiu_buttton = (By.XPATH, "//input[@type='radio' and @data-type='3']")
    # 巡检button
    xunjian_buttton = (By.XPATH, "//input[@type='radio' and @data-type='4']")
    # 请选择派发流程select
    dispatch_flow_select = (By.XPATH, "//span[contains(text(), '请选择派发流程')]/following-sibling::div[1]/div/div/input[2]")
    # 请选择派发流程select下拉菜单
    dispatch_flow_selected_one = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[4]")
    # 项目名称input
    project_name_input = (By.XPATH, "//span[contains(text(), '项目名称')]/following-sibling::div[1]/div/input[1]")
    # 项目地点input
    project_place_input = (By.XPATH, "//span[contains(text(), '项目地点')]/following-sibling::div[1]/div/input[1]")
    # 负责人select下拉菜单
    principal_select = (By.XPATH, "//span[contains(text(), '负责人')]/following-sibling::div[1]/div/div/input[2]")
    # 请选择负责人select下拉菜单
    principal_selected_one = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[4]")
    # 验证人select下拉菜单
    identifier_select = (By.XPATH, "//span[contains(text(), '验证人')]/following-sibling::div[1]/div/div/input[2]")
    # 客户select下拉菜单
    # customer_selects = (By.XPATH, "//li[contains(text(), '试用用户')]")
    customer_selects = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[1]")
    # 客户联系人input
    # 联系电话input
    # 工单内容描述input
    # 计划开始时间select
    # 计划结束时间select
    # 班组输入input

    # 我的待办button
    my_to_do_button = (By.XPATH, "//div[contains(text(), '我的待办')]")
    # 第一个处理button
    deal_button = (By.XPATH, "//span[contains(text(), '处理')]")
    # 所需仪器input
    instrument_required_input = (By.XPATH, "//span[contains(text(), '所需仪器')]/following-sibling::span[1]/div/input")
    # 所需材料input
    material_required_input = (By.XPATH, "//span[contains(text(), '所需材料')]/following-sibling::span[1]/div/input")
    # 抢修计划input
    repair_plan_input = (By.XPATH, "//span[contains(text(), '抢修计划')]/following-sibling::span[1]/div/textarea")
    # 处理结果input
    deal_result_input = (By.XPATH, "//span[contains(text(), '处理结果')]/following-sibling::span[1]/div/textarea")
    # 审核button
    audit_button = (By.CLASS_NAME, "audit")
    # 结果描述input
    result_description_input = (By.XPATH, "//span[contains(text(), '结果描述')]/following-sibling::span[1]/div/textarea")
    # 弹窗通过button
    pass_button = (By.XPATH, "//button[contains(text(), '通过')]")
    # 弹窗不通过button
    no_pass_button = (By.XPATH, "//button[contains(text(), '不通过')]")
    # 弹窗提示取消button
    hint_cancel_button = (By.XPATH, '//*[@id="job"]/div/div[3]/div/div[2]/button[1]')
    # 弹窗提示再次派单button
    hint_again_dispatch_button = (By.XPATH, '//*[@id="job"]/div/div[3]/div/div[2]/button[2]')

    def click_my_to_do_button(self, driver):
        driver.find_element(*self.my_to_do_button).click()

    def click_first_deal_button(self, driver):
        driver.find_elements(*self.deal_button)[1].click()

    def input_audit_form(self, driver, required_equipment, required_materials, repaired_plan):
        driver.find_element(*self.instrument_required_input).send_keys(required_equipment)
        driver.find_element(*self.material_required_input).send_keys(required_materials)
        driver.find_element(*self.repair_plan_input).send_keys(repaired_plan)
        driver.find_element(*self.audit_button).click()

    def input_deal_form(self, driver, deal_result):
        driver.find_element(*self.deal_result_input).send_keys(deal_result)
        driver.find_element(*self.audit_button).click()

    def input_verify_form(self, driver, result_description):
        driver.find_element(*self.result_description_input).send_keys(result_description)

    def click_vertify_form_pass_button(self, driver):
        driver.find_element(*self.pass_button).click()

    def click_vertify_form_no_pass_button(self, driver):
        driver.find_element(*self.no_pass_button).click()

    def click_hint_cancel_button(self, driver):
        driver.find_element(*self.hint_cancel_button).click()

    def click_hint_again_dispatch_button(self, driver):
        driver.find_element(*self.hint_again_dispatch_button).click()

    def click_add_order(self, driver):
        driver.find_element(*self.add_order_button).click()

    def click_qiangxiu_button(self, driver):
        driver.find_element(*self.qiangxiu_button).click()

    def click_shiyan_button(self, driver):
        driver.find_element(*self.shiyan_button).click()

    def click_weixiu_buttton(self, driver):
        driver.find_element(*self.weixiu_buttton).click()

    def click_xunjian_buttton(self, driver):
        driver.find_element(*self.xunjian_buttton).click()

    def click_dispatch_flow_select(self, driver):
        driver.find_element(*self.dispatch_flow_select).click()

    def click_dispatch_flow_selected_one(self, driver):
        driver.find_element(*self.dispatch_flow_selected_one).click()

    def input_project_name(self, driver, project_name):
        driver.find_element(*self.project_name_input).send_keys(project_name)

    def input_project_place(self, driver, project_place):
        driver.find_element(*self.project_place_input).send_keys(project_place)

    def click_principal_select(self, driver):
        driver.find_element(*self.principal_select).click()

    def click_principal_selected_one(self, driver):
        el = driver.find_elements(*self.customer_selects)
        el[1].click()
