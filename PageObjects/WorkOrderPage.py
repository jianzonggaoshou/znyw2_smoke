# coding=utf-8
from selenium.webdriver.common.by import By


class WorkOrderPage(object):
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
