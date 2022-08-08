from selenium.webdriver.common.by import By

from pageObjects.AssignmentPage import AssignmentPage
from pageObjects.ManageCoursePage import ManageCoursePage
from pageObjects.ManageUserPage import ManageUserPage
from pageObjects.NewAssignmentPage import NewAssignmentPage
from pageObjects.QuestionPoolPage import QuestionPoolPage
from pageObjects.QuestionsPage import QuestionsPage
from pageObjects.RolePage import RolePage



class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    tab_button = (By.XPATH, "//button/a")
    tabs = (By.CLASS_NAME, "buttons_buttonContainer__QIjDv MuiBox-root css-0")
    view_roles = (By.XPATH, "//span[text()='View Roles']")
    create_role = (By.XPATH, "//span[text()='Create Role']")
    manage_course = (By.XPATH, "//span[text()='Manage Course']")
    manage_users = (By.XPATH, "//span[text()='Manage Users']")
    question_pool = (By.XPATH, " //div[6]//button[2]//*[name()='svg']")
    assignment_but = (By.LINK_TEXT, "ASSIGNMENT")
    c_ass_admin_but =(By.XPATH, "(//button[@id='basic-button'])[3]")
    new_assignment_but = (By.LINK_TEXT, "+ New Assignment")
    questions_but = (By.LINK_TEXT,"QUESTIONS")
    course_svg = (By.XPATH,"//div[3]//button[2]//*[name()='svg']")


    def get_tab_buttons(self):
        return self.driver.find_elements(*DashboardPage.tab_button)

    def view_role(self):
        self.driver.find_element(*DashboardPage.view_roles).click()
        rolePage = RolePage(self.driver)
        return rolePage

    def create_role(self):
        self.driver.find_element(*DashboardPage.create_role).click()

    def manage_user(self):
        self.driver.find_element(*DashboardPage.manage_users).click()
        return ManageUserPage(self.driver)

    def go_to_ques_pool(self):
        self.driver.find_element(*DashboardPage.question_pool).click()
        self.driver.find_element(By.LINK_TEXT,"Question Pool").click()
        return QuestionPoolPage(self.driver)

    def go_to_assignment(self):
        self.driver.find_element(*DashboardPage.assignment_but).click()
        return AssignmentPage(self.driver)

    def create_assignment_admin(self):
        self.driver.find_element(*DashboardPage.c_ass_admin_but).click()
        self.driver.find_element(*DashboardPage.new_assignment_but).click()
        return NewAssignmentPage(self.driver)

    def go_to_question(self):
        self.driver.find_element(*DashboardPage.questions_but).click()
        return QuestionsPage(self.driver)

    def go_to_mangage_course(self):
        self.driver.find_element(*DashboardPage.course_svg).click()
        self.driver.find_element(By.LINK_TEXT, "Manage Courses").click()
        return ManageCoursePage(self.driver)








