# -*- coding: utf-8 -*-
import datetime
import os
import unittest
import urlparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class Page(object):
    BASE_URL = 'https://calendar.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

class AuthPage(Page):
    @property
    def form(self):
        return AuthForm(self.driver)

class CalendarPage(Page):
    @property
    def tasks(self):
        return TasksForm(self.driver)

class Component(object):
    def __init__(self, driver):
        self.driver = driver

class AuthForm(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD_INPUT = '//input[@name="Password"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'
    SUBMIT_ACCOUNT_NAME = '//button[@data-test-id="next-button"]'

    def set_login(self, login):
        WebDriverWait(self.driver, 60).until(
            lambda d: d.find_element_by_xpath(self.LOGIN)
        )
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        # wait = WebDriverWait(self.driver, 60)
        # element = wait.until(self.driver.find_element_by_xpath(self.PASSWORD_INPUT))
        # element.send_keys(pwd)
        WebDriverWait(self.driver, 60).until(
            lambda d: d.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(pwd)
        )
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(pwd)

    def submit_account_name(self):
        print('submitAccountName')
        self.driver.find_element_by_xpath(self.SUBMIT_ACCOUNT_NAME).click()

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

class TasksForm(Component):
    TASK = '//input[@name="summary"]'
    TODO = '//div[contains(@class, "todo")]'
    CREATE_EVENT_BUTTON = '//a[contains(@class, "button_create-event")]'
    SAVE_EVENT_BUTTON = '//a[contains(@class, "event-new__button_submit")]'
    CANCEL_EVENT_BUTTON = '//a[contains(@class, "event-new__reset")]'
    ATTENDEES_CONTAINER = '//div[@class="attendees-selector__textbox"]'
    ATTENDEES = './/input'

    def set_task(self, task_topic):
        self.driver.find_element_by_xpath(self.TASK).send_keys(task_topic)

    def get_tasks_list(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT)
        )

    def add_attendees(self, email):
        container = self.driver.find_element_by_xpath(self.ATTENDEES_CONTAINER)
        input_field = container.find_element_by_xpath(self.ATTENDEES)
        input_field.send_keys(email)
        # container.find_element_by_xpath(self.ATTENDEES).send_keys(Keys.ENTER)

    def create_event(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_EVENT_BUTTON).click()
        )
        # self.driver.find_element_by_xpath(self.CREATE_EVENT_BUTTON).click()

    def save_event(self):
        self.driver.find_element_by_xpath(self.SAVE_EVENT_BUTTON).click()


class BusinessCreationTest(unittest.TestCase):
    #LOGIN = environ['LOGIN'] 
    USEREMAIL = os.environ['LOGIN']
    PASSWORD = str(os.environ['PASSWORD'])
    TASK_TOPIC = 'TEST_TASK' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def setUp(self):
        browser_name = os.environ['BROWSER']
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={
                "browserName": browser_name,
            }
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        # Вход
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.submit_account_name()
        auth_form.set_password(self.PASSWORD)
        # auth_form.submit()

        cal_page = CalendarPage(self.driver) # Открыть страницу календаря
        
        # Создается событие с другими участниками.
        # Создается событие длительностью более дня.
        # Создается события с указанием названия.
        # Создается события с указанием места.
        # Создается события с указанием описания.
        # Удалить событие?
        
        tasks_wrapper = cal_page.tasks
        tasks_wrapper.create_event()
        USEREMAIL = 'qwertyqwerty123228@mail.ru'
        tasks_wrapper.add_attendees(USEREMAIL)
        tasks_wrapper.save_event()
        
        # tasks_wrapper.set_task(self.TASK_TOPIC)
        # tasks_wrapper.add_task()

        # tasks_list = tasks_wrapper.get_tasks_list()
        # print('el: ' + tasks_list)
