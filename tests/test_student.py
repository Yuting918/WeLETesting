import logging
import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.AddRolePage import AddRolePage
from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from testData.AsStudentTestData import AsStudentTestData
from utilities.BaseClass import BaseClass


class TestTakeAssignment(BaseClass):
    course_name = 'TestCourse003'
    assignment_name = course_name + '_Ass_002'

    def test_stu_take_ass(self, getData):
        stu_id = getData['ID']
        student = 'StuFName' + stu_id + ' StuLName' + stu_id
        answer = getData['Answer']
        # log in as student
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole(student)
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        tabs = dashboard.get_tab_buttons()
        tabs_l = []
        for tab in tabs:
            tabs_l.append(tab.text)
        log.info(tabs_l)

        # taking the test
        assignmentPage = dashboard.go_to_assignment()
        assignmentPage.choose_course(TestTakeAssignment.course_name)
        try:
            assignmentPage.zero_remaining_attempts(
                TestTakeAssignment.assignment_name)
        except:
            log.info('Answer Test')
            takingAssPage = assignmentPage.go_to_spec_ass(
                TestTakeAssignment.assignment_name)
            ass_info = takingAssPage.get_assignment_info()
            log.info(f'The assignment name is {ass_info[0]}; The type is '
                     f'{ass_info[1]}; The number of questions is {ass_info[2]}; '
                     f'The time limit is {ass_info[3]}')
            takingAssPage.type_answer(answer)
            takingAssPage.submit_assignment()
            time.sleep(2)
            takingAssPage.confirm_submit()
            time.sleep(2)
            ass_r_info = takingAssPage.get_assignment_review()
            log.info(ass_r_info)
            self.get_scores(assignmentPage, log,student)
            self.logout()
        else:
            log.warning(
                'There is no attempt left for' + TestTakeAssignment.assignment_name)
            self.get_scores(assignmentPage, log,student)
            self.logout()

    def test_stu_take_ass_timer(self, getData):
        stu_id = getData['ID']
        student = 'StuFName' + stu_id + ' StuLName' + stu_id
        # log in as student
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole(student)
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        tabs = dashboard.get_tab_buttons()
        tabs_l = []
        for tab in tabs:
            tabs_l.append(tab.text)
        log.info(tabs_l)

        # taking the test
        assignmentPage = dashboard.go_to_assignment()
        assignmentPage.choose_course(TestTakeAssignment.course_name)
        try:
            assignmentPage.zero_remaining_attempts(
                TestTakeAssignment.assignment_name)
        except:
            log.info('Time out test')
            takingAssPage = assignmentPage.go_to_spec_ass(
                TestTakeAssignment.assignment_name)

            ass_info = takingAssPage.get_assignment_info()
            log.info(f'The assignment name is {ass_info[0]}; The type is '
                     f'{ass_info[1]}; The number of questions is {ass_info[2]}; '
                     f'The time limit is {ass_info[3]}')
            time_in_min = int(ass_info[3].split(' Minutes')[0])
            time_in_sec = time_in_min * 60
            time.sleep(time_in_sec + 5)
            ass_r_info = takingAssPage.get_assignment_review()
            log.info(ass_r_info)
            actual_time_string = ass_r_info[5]
            actual_time_h = int(actual_time_string.split('h')[0])
            actual_time_m = int(
                (actual_time_string.split('h ')[1]).split('min')[0])
            actual_time_s = int(
                ((actual_time_string.split('h ')[1]).split('min '
                                                           '')[1]).split('sec')[
                    0])
            actual_time_in_sec = actual_time_h * 60 * 60 + actual_time_m * 60 + actual_time_s
            assert abs(actual_time_in_sec - time_in_sec) < 10
            self.get_scores(assignmentPage, log,student)
            self.logout()
        else:
            log.warning(
                'There is no attempt left for' + TestTakeAssignment.assignment_name)
            self.get_scores(assignmentPage, log,student)
            self.logout()

    def get_scores(self, assignmentPage, log,student):
        scoresPage = assignmentPage.go_to_score_page()
        scoresPage.choose_course(TestTakeAssignment.course_name)
        scoresPage.set_end_date()
        scoresPage.fetch_score()
        score_rows = scoresPage.get_score_rows()
        for score_row in score_rows:
            log.info('fetch scores...')
            if score_row.find_element(By.XPATH, ".//td[1]//span").text == \
                    TestTakeAssignment.assignment_name:
                score = score_row.find_element(By.XPATH, ".//td[2]//span").text
                log.info('Student '+ student +': the scores for ' \
                                                       'course' +
                         TestTakeAssignment.course_name + ' '
                         'assignment ' + TestTakeAssignment.assignment_name + ' is ' + score)

    @pytest.fixture(params=AsStudentTestData.gen_id_answer(8, 10, ['-3/(x^4)',
                                                                  '8x^7 +Cos[x]']))
    def getData(self, request):
        return request.param
