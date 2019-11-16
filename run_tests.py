# -*- coding: utf-8 -*-
import unittest
import os

from selenium import webdriver
from steps.auth import *
from steps.calendar import *

class TestClass(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser_name = os.environ['BROWSER']
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={
                "browserName": browser_name,
            }
        )
        login(self)

    def tearDown(self):
        self.driver.quit()

    # Создается событие с другими участниками.
    def test_create_event_w_attendees(self):
        is_saved_successfully = True
        result = set_create_event_w_attendees(self)
        self.assertEqual(is_saved_successfully, result)
        
    # Создается событие длительностью более дня
    def test_create_event_2_day_duration(self):
        is_saved_successfully = True
        result = set_create_event_2_day_duration(self)
        self.assertEqual(is_saved_successfully, result)
        
    # Создается события с указанием названия
    def test_mcreate_event_w_name(self):
        is_saved_successfully = True
        result = set_create_event_w_name(self)
        self.assertEqual(is_saved_successfully, result)

    # Создается события с указанием места
    def test_create_event_w_location(self):
        is_saved_successfully = True
        result = set_create_event_w_location(self)
        self.assertEqual(is_saved_successfully, result)

    # Создается события с указанием описания
    def test_create_event_w_description(self):
        is_saved_successfully = True
        result = set_create_event_w_description(self)
        self.assertEqual(is_saved_successfully, result)
        
    # # Сохраняются нестандартные настройки напоминаний для новых событий. URL:https://calendar.mail.ru/ Ошибка:http://jira.bmstu.cloud/browse/QA-277
    # Хм. Трудновато проверить т.к. надо найти созданное событие на всей сетке

    # # Может быть выслано напоминание о событии по почте не меньше чем за минуту до самого события. URL:https://calendar.mail.ru/ Ошибка:http://jira.bmstu.cloud/browse/QA-280
    # Странный кейс. Напоминание МОЖЕТ быть выслано в тот же момент, что и событие

if __name__ == '__main__':
    unittest.main()
