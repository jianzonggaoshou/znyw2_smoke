# coding=utf-8
from selenium.webdriver.common.by import By
from time import sleep


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
    """select1"""
    # 请选择派发流程select
    dispatch_flow_select = (By.XPATH, "//span[contains(text(), '请选择派发流程')]/following-sibling::div[1]/div/div/input[2]")
    # 请选择派发流程select下拉菜单
    dispatch_flow_selected_one = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[4]")
    """select1"""
    # 项目名称input
    project_name_input = (By.XPATH, "//span[contains(text(), '项目名称')]/following-sibling::div[1]/div/input[1]")
    # 项目地点input
    project_place_input = (By.XPATH, "//span[contains(text(), '项目地点')]/following-sibling::div[1]/div/input[1]")
    """select2"""
    # 负责人select下拉菜单
    principal_select = (By.XPATH, "//span[contains(text(), '负责人')]/following-sibling::div[1]/div/div/input[2]")
    # 负责人下拉菜单列表-第一个选项
    principal_selected_lists = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[1]")
    """select2"""
    # 验证人select下拉菜单
    identifier_select = (By.XPATH, "//span[contains(text(), '验证人')]/following-sibling::div[1]/div/div/input[2]")
    # 验证人select下拉菜单列表-第一个选项
    identifier_selected_list = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[1]")
    """select3"""
    # 客户select下拉菜单-选择第一个用户
    customer_select = (By.XPATH, "//span[contains(text(), '客户')]/following-sibling::div[1]/div/div/input[2]")
    # 客户select下拉菜单列表-最后一个选项
    customer_selected_lists = (By.XPATH, "//ul[@class='ivu-select-dropdown-list']/li[2]")
    # 客户联系人input
    customer_linkman_input = (By.XPATH, "//span[contains(text(), '客户联系人')]/following-sibling::div[1]/div/input[1]")
    # 联系电话input
    linkman_tel_input = (By.XPATH, "//span[contains(text(), '联系电话')]/following-sibling::div[1]/div/input[1]")
    # 工单内容描述input
    work_order_content_description_input = (By.XPATH, "//span[contains(text(), '工单内容描述')]/following-sibling::div[1]/div/textarea")

    # 计划开始时间input
    plan_start_time_js = 'document.getElementsByTagName("input")[16].removeAttribute("readonly");'
    plan_start_time_input = (By.XPATH, "//span[contains(text(), '计划开始时间')]/following-sibling::div[1]/div/div/div/input[1]")
    # 计划时间确定button
    plan_confirm_button1 = (By.XPATH, '//span[contains(text(), "确定")]')
    plan_confirm_button2 = (By.XPATH, '//span[contains(text(), "确定")]')
    # 计划结束时间input
    plan_end_time_js = 'document.getElementsByTagName("input")[17].removeAttribute("readonly");'
    plan_end_time_input = (By.XPATH, "//span[contains(text(), '计划结束时间')]/following-sibling::div[1]/div/div/div/input")
    # 班组输入input
    group_input = (By.XPATH, "//span[contains(text(), '班组')]/following-sibling::div[1]/div/input[1]")
    # 派单button
    dispatch_button = (By.XPATH, "//button[contains(text(), '派单')]")


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
        el = driver.find_elements(*self.principal_selected_lists)
        el[1].click()

    def click_identifier_select(self, driver):
        driver.find_element(*self.identifier_select).click()

    def click_identifier_selected_one(self, driver):
        el = driver.find_elements(*self.identifier_selected_list)
        el[2].click()

    def click_customer_select(self, driver):
        driver.find_element(*self.customer_select).click()

    def click_customer_selected_one(self, driver):
        el = driver.find_elements(*self.customer_selected_lists)
        el[3].click()

    def input_customer_linkman(self, driver, customer_linkman):
        driver.find_element(*self.customer_linkman_input).send_keys(customer_linkman)

    def input_linkman_tel(self, driver, linkman_tel):
        driver.find_element(*self.linkman_tel_input).send_keys(linkman_tel)

    def input_work_order_content_description(self, driver, work_order_content_description):
        driver.find_element(*self.work_order_content_description_input).send_keys(work_order_content_description)

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

    def input_group(self, driver, group):
        driver.find_element(*self.group_input).send_keys(group)

    def click_dispatch_button(self, driver):
        driver.find_element(*self.dispatch_button).click()
