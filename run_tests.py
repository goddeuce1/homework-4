# -*- coding: utf-8 -*-
# import time
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

# При выборе начала и конца рабочего дня настройки успешно сохраняются.
    def test_workday_times(self):
        is_saved_successfully = True
        result = set_workday_times(self)
        self.assertEqual(is_saved_successfully, result)

# При выборе основного календаря настройки успешно сохраняются.
    def test_main_calendar(self):
        is_saved_successfully = True
        result = set_main_calendar(self)
        self.assertEqual(is_saved_successfully, result)

# При выборе хотя бы двух рабочих дней настройки успешно сохраняются.
    def test_two_workdays(self):
        is_saved_successfully = True
        result = set_two_workdays(self)
        self.assertEqual(is_saved_successfully, result)

# При выборе ни одного рабочего дня настройки не сохраняются.
    def test_zero_workdays(self):
        is_saved_successfully = False
        result = set_zero_workdays(self)
        self.assertEqual(is_saved_successfully, result)

# Настройки успешно сохраняются при разрешении хотя бы одного способа напоминания о событии.
    def test_one_reminder(self):
        is_saved_successfully = True
        result = set_one_reminder(self)
        self.assertEqual(is_saved_successfully, result)

# Настройки успешно сохраняются при запрете всех способов напоминания о событии.
    def test_zero_reminders(self):
        is_saved_successfully = True
        result = set_zero_reminders(self)
        self.assertEqual(is_saved_successfully, result)

# Успешное сохранение настроек при отключении всех звуков в браузере.
    def test_mute_sound(self):
        is_saved_successfully = True
        result = set_sound_muted(self)
        self.assertEqual(is_saved_successfully, result)

# Успешное сохранение настроек при отметке всех вариантов получения уведомлений по электронной почте.
    def test_all_email_reminders(self):
        is_saved_successfully = True
        result = set_all_email_reminders(self)
        self.assertEqual(is_saved_successfully, result)

# Успешное сохранение настроек при выборе ни одного варианта уведомления по электронной почте.
    def test_zero_email_reminders(self):
        is_saved_successfully = True
        result = set_zero_email_reminders(self)
        self.assertEqual(is_saved_successfully, result)


if __name__ == '__main__':
    unittest.main()
