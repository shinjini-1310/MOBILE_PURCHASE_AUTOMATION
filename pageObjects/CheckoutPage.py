from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import Confirm_Page

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    mobiles = (By.CSS_SELECTOR, ".card-title a")
    footers = (By.CSS_SELECTOR,".card-footer button")
    checkout_button = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    final_checkout_button = (By.CSS_SELECTOR, ".btn.btn-success")

    def get_mobile_names_list(self):
        return self.driver.find_elements(*CheckoutPage.mobiles)
    def get_card_footer_button(self):
        return self.driver.find_elements(*CheckoutPage.footers)
    def get_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)
    def get_final_checkout_button(self):
        self.driver.find_element(*CheckoutPage.final_checkout_button).click()
        cp = Confirm_Page(self.driver)
        return cp


