from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name= (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox1 = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    success_btn = (By.CSS_SELECTOR,".btn.btn-success")
    success_alert = (By.CLASS_NAME,"alert-success")

    def shop_click(self):
        self.driver.find_element(*HomePage.shop).click()
        mobiles = CheckoutPage(self.driver)
        return mobiles

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox1(self):
        return self.driver.find_element(*HomePage.checkbox1)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_success_btn(self):
        return self.driver.find_element(*HomePage.success_btn)

    def get_success_alert(self):
        return self.driver.find_element(*HomePage.success_alert)








