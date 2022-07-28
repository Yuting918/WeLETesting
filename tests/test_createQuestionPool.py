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
        questionPoolPage = dashboard.go_to_ques_pool()
        self.delete_all_pools(questionPoolPage,log)
        questionPoolPage.add_pool()
        question_pool_names = QuestionPoolData.pool_name_generator(1)
        log.info(question_pool_names)
        i = 0
        for p_name in question_pool_names:
            if i == 0:
                questionPoolPage.create_pool(p_name, 'TestPool',1)
            else:
                questionPoolPage.create_another_pool(p_name, 'TestPool',1)
            i += 1
        questionPoolPage.add_question()
        questionPoolPage.choose_tag('MATH 101')
        questionPoolPage.fetch_questions()
        self.add_all_questions(questionPoolPage,log)
        self.driver.find_element(By.TAG_NAME,'body').send_keys(
            Keys.CONTROL + Keys.HOME)
        self.driver.maximize_window()
        questionPoolPage.update_pool()




    def delete_all_pools(self,questionPoolPage,log):
        while True:
            try:
                questionPoolPage.get_alert()
                log.info('No question pool fetched')
                break
            except:
                questionPoolPage.view_pool()
                time.sleep(0.5)
                questionPoolPage.delete_pool()
                time.sleep(0.5)

    def add_all_questions(self,questionPoolPage,log):
        while True:
            try:
                questionPoolPage.get_alert()
                log.info('No question fetched')
                break
            except:
                questionPoolPage.click_add()