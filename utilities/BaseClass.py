import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import inspect
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_linktext_presence(self,text):
        wait = WebDriverWait(self.driver, 10)
        # wait until CSS selectors presence is located in the webpage
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))
    def select_gender_from_dropdown(self,locator,text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def get_Logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('INSERT DESIRED LOGFILE LOCATION')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object. Logger obj is asking in which file should it log and whats the format?
        logger.setLevel(logging.DEBUG)
        return logger

