import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.AddRolePage import AddRolePage
from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from testData.QuestionPoolData import QuestionPoolData
from utilities.BaseClass import BaseClass

class TestWeLEAdmin(BaseClass):
    course_name: str = 'TestCourse004'
    user_start_id = 12
    user_end_id = 15
    pool_tag = 'MATH 101'
    pool_name = 'TestPool000'
    assignment_name = course_name + '_Ass_001'
    assignment_type='Homework'
    add_timer = True
    assignment_max_temp = 3
    assignment_duration = 1
    assignment_due_date = '08202022'
    assignment_due_date_extd = '08202022'
    assignment_grade_method = 'Max'

    def test_admin_create_course(self, course_name=course_name):
        # log in as admin
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        manageCoursePage = dashboard.go_to_mangage_course()
        manageCoursePage.add_new_course()
        manageCoursePage.create_course(course_name, 'Fall', 'TestTA',
                                       course_name + '_ID',
                                       "TestInstructor")
        self.logout()

    def test_admin_add_user(self, s=user_start_id, e=user_end_id):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        manageUserPage = dashboard.manage_user()
        manageUserPage.add_user('student')
        users = NewUserData.gen_user('Stu', s, e)

        for user in users:
            time.sleep(2)
            manageUserPage.get_ID().send_keys(user['ID'])
            manageUserPage.get_f_name().send_keys(user['f_name'])
            manageUserPage.get_l_name().send_keys(user['l_name'])
            log.info(user['ID'] + 'successfully added')
            time.sleep(2)
            manageUserPage.submit_add_user()
        self.logout()

    def test_admin_add_user_to_course(self, course_name=course_name,
                                      s=user_start_id, e=user_end_id):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        manageUserPage = dashboard.manage_user()
        users = NewUserData.gen_user('Stu', s, e)

        for user in users:
            manageUserPage.select_user(user['f_name'], user['l_name'])
            manageUserPage.select_course(course_name)
            time.sleep(1)
            popped_course = manageUserPage.get_popped_course()
            log.info('the popped course is: ' + popped_course)
            assert course_name in popped_course
            manageUserPage.submit_register_user()
            time.sleep(1)
            manageUserPage.sort_user()
            time.sleep(1)
            manageUserPage.sort_user()
            time.sleep(1)
            assert user['f_name'] in manageUserPage.get_registered_user(user[
                                                                            'f_name'])
            log.info(user['f_name'] + 'successfully added to' + course_name)
            self.driver.refresh()
            time.sleep(1)
        manageUserPage.logout()

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
        self.delete_all_pools(questionPoolPage, log)
        questionPoolPage.add_pool()
        question_pool_names = QuestionPoolData.pool_name_generator(2)
        log.info(question_pool_names)
        i = 0
        for p_name in question_pool_names:
            if i == 0:
                questionPoolPage.create_pool(p_name, 'TestPool', 2)
            else:
                questionPoolPage.create_another_pool(p_name, 'TestPool', 2)
            i += 1
        questionPoolPage.add_question()
        questionPoolPage.choose_tag(TestWeLEAdmin.pool_tag)
        questionPoolPage.fetch_questions()
        self.add_all_questions(questionPoolPage, log)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(
            Keys.CONTROL + Keys.HOME)
        self.driver.maximize_window()
        questionPoolPage.update_pool()
        self.logout()

    def test_release_question_pool(self, course_name=course_name):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        newAssignmentPage = dashboard.create_assignment_admin()
        newAssignmentPage.choose_from_q_pool()
        newAssignmentPage.get_pool_by_name(TestWeLEAdmin.pool_name)
        assignmentConfigurePage = newAssignmentPage.save_and_proceed()
        assignmentConfigurePage.configure_assignment(course_name,
                                                     TestWeLEAdmin.assignment_name,
                                                     TestWeLEAdmin.assignment_max_temp,
                                                     TestWeLEAdmin.assignment_type,
                                                     TestWeLEAdmin.add_timer,
                                                     TestWeLEAdmin.assignment_duration,
                                                     TestWeLEAdmin.assignment_due_date,
                                                     TestWeLEAdmin.assignment_due_date_extd,
                                                     TestWeLEAdmin.assignment_grade_method)
        assignmentConfigurePage.save_and_proceed()
        assignmentConfigurePage.release_assignment()
        log.info('Assignment successfully released')

    def delete_all_pools(self,questionPoolPage,log):
        while True:
            try:
                questionPoolPage.get_alert()
                log.info('No question pool fetched')
                break
            except:
                questionPoolPage.view_pool()
                time.sleep(1)
                try:
                    questionPoolPage.pool_editable()
                    log.info('This question pool is not editable')
                    questionPoolPage.go_back()
                    break
                except:
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