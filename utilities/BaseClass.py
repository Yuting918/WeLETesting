import inspect
import logging

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# now the base class have the knowledge of the setup
@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.INFO)
        return logger


    def verifyAutoCompleteUserPresence(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "input[aria-controls='autocomplete-user-field-listbox']"))) \
            .send_keys(Keys.ARROW_DOWN)

    def verifyDropdownPresence(self,text):
        path = "//ul/li[text()='" + text + "']"
        self.getLogger().info(path)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(
            (By.XPATH,path))).click()


    def verifyADLPresence(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "input[aria-controls='asynchronous-demo-listbox']"))) \
            .send_keys(Keys.ARROW_DOWN)

    def verifyAutoCompleteCoursePresence(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "input[aria-controls='autocomplete-course-field-listbox']"))) \
            .send_keys(Keys.ARROW_DOWN)

    def triple_click(self,source):
        actions = ActionChains(self.driver)
        for i in range(3):
            actions.click(source).perform

    def logout(self):
        self.driver.find_element(By.XPATH,"//button[text()='Logout']").click()
