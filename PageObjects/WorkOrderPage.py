# coding=utf-8
from selenium.webdriver.common.by import By


class WorkOrderPage(object):
    def __init__(self):
        self.my_to_do_button = "//div[contains(text(), '我的待办')]"
        self.deal_button = "//span[contains(text(), '处理')]"
        self.instrument_required_input = "//span[contains(text(), '所需仪器')]/following-sibling::span[1]/div/input"
        self.material_required_input = "//span[contains(text(), '所需材料')]/following-sibling::span[1]/div/input"
        self.repair_plan_input = "//span[contains(text(), '抢修计划')]/following-sibling::span[1]/div/textarea"
        self.deal_result_input = "//span[contains(text(), '处理结果')]/following-sibling::span[1]/div/textarea"
        self.audit_button = "audit"
        self.result_description_input = "//span[contains(text(), '结果描述')]/following-sibling::span[1]/div/textarea"
        self.pass_button = "//button[contains(text(), '通过')]"
        self.no_pass_button = "//button[contains(text(), '不通过')]"

    def click_my_to_do_button(self, driver):
        driver.find_element(By.XPATH, self.my_to_do_button).click()

    def click_first_deal_button(self, driver):
        driver.find_elements(By.XPATH, self.deal_button)[1].click()

    def input_audit_form(self, driver, required_equipment, required_materials, repaired_plan):
        driver.find_element(By.XPATH, self.instrument_required_input).send_keys(required_equipment)
        driver.find_element(By.XPATH, self.material_required_input).send_keys(required_materials)
        driver.find_element(By.XPATH, self.repair_plan_input).send_keys(repaired_plan)
        driver.find_element(By.CLASS_NAME, self.audit_button).click()

    def input_deal_form(self, driver, deal_result):
        driver.find_element(By.XPATH, self.deal_result_input).send_keys(deal_result)
        driver.find_element(By.CLASS_NAME, self.audit_button).click()

    def input_verify_form(self, driver, result_description):
        driver.find_element(By.XPATH, self.result_description_input).send_keys(result_description)

    def click_vertify_form_pass_button(self, driver):
        driver.find_element(By.XPATH, self.pass_button).click()

    def click_vertify_form_no_pass_button(self, driver):
        driver.find_element(By.XPATH, self.no_pass_button).click()
