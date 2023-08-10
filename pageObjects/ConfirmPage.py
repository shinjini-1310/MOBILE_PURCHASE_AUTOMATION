from selenium.webdriver.common.by import By

class Confirm_Page:

    def __init__(self, driver):
        self.driver = driver

    country_box = (By.CSS_SELECTOR, "#country")
    link_text = (By.LINK_TEXT, "India")
    t_and_c = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    purchase_btn=(By.CSS_SELECTOR,'.btn.btn-success.btn-lg')
    success_alert_text = (By.CSS_SELECTOR,'.alert.alert-success')

    def get_country_names(self):
        return self.driver.find_element(*Confirm_Page.country_box)

    def get_linktext(self):
        return self.driver.find_element(*Confirm_Page.link_text)

    def terms_and_conditions_agree(self):
        return self.driver.find_element(*Confirm_Page.t_and_c)

    def get_purchase_btn(self):
        return self.driver.find_element(*Confirm_Page.purchase_btn)

    def get_success_alert_text(self):
        return self.driver.find_element(*Confirm_Page.success_alert_text)

