import time
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_Logger()
        home_page=HomePage(self.driver)
        mobiles = home_page.shop_click()
        log.info("GETTING ALL THE CARD TITLES")
         mobile_names = mobiles.get_mobile_names_list()
        i=-1
        for mob in mobile_names:
            i+=1
            mob_nm = mob.text
            log.info(mob_nm)
            if mob_nm == 'Blackberry':
                mobiles.get_card_footer_button()[i].click()
                break
        mobiles.get_checkout_button().click()
        time.sleep(2)
        cp = mobiles.get_final_checkout_button()
        time.sleep(2)
        log.info("ENTERING COUNTRY NAME PARTIALLY")
        cp.get_country_names().send_keys("ind")
        self.verify_linktext_presence("India")
        cp.get_linktext().click()
        time.sleep(2)
        cp.terms_and_conditions_agree().click()
        time.sleep(2)
        cp.get_purchase_btn().click()
        time.sleep(2)
        success_text = cp.get_success_alert_text().text
        log.info("TEXT RECEIVED FROM APPLICATION ALERT")
        log.info(success_text)
        #assert "Success" in success_text
        assert "QWERTY" in success_text
