import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from testData.QuestionPoolData import QuestionPoolData
from utilities.BaseClass import BaseClass

class TestGenQuesPool(BaseClass):
    def test_generate_question_pool(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        questionPoolPage = dashboard.go_to_ques_pool(screenshot=True,fileName='/Users/yutingq/Desktop/lms_was_testing/deleteQuestionPool/'
            'before_deletion.png')
        self.delete_all_pools(questionPoolPage,log)



    def delete_all_pools(self,questionPoolPage,log):
        while True:
            try:
                questionPoolPage.get_alert()
                log.info('No question pool fetched')
                break
            except:
                questionPoolPage.view_pool()
                try:
                    questionPoolPage.pool_editable()
                    log.info('This question pool is not editable')
                    questionPoolPage.go_back()
                    break
                except:
                    questionPoolPage.delete_pool()



