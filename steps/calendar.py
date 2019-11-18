from pages.calendar import *
from selenium.common.exceptions import NoSuchElementException
from datetime import timedelta

def set_create_event_w_attendees(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.add_attendees("iergeoi@e.mail.ru")
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False

def set_create_event_2_day_duration(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    date = calendar.get_date_end()
    calendar.set_date_end(date + timedelta(days = 2))
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False

def set_create_event_w_name(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.set_name("test name")
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False

def set_create_event_w_location(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.set_location("test location")
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False

def set_create_event_w_description(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.set_description("test description")
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False


def set_workday_times(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.change_workday_times()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_main_calendar(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.change_calendar()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_two_workdays(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.change_to_two_workdays()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_zero_workdays(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.change_to_zero_workdays()
    calendar.settings_submit()

    try:
        calendar.driver.find_element_by_xpath(calendar.WORKDAY_CHECKBOX_ERROR)
    except NoSuchElementException:
        return True

    return False


def set_one_reminder(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.change_to_one_reminder()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_zero_reminders(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.change_to_zero_reminders()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_sound_muted(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.mute_sound()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_all_email_reminders(self):
    select_all_state = 'true'
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.change_email_reminders(select_all_state)
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_zero_email_reminders(self):
    select_all_state = 'false'
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.change_email_reminders(select_all_state)
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False
