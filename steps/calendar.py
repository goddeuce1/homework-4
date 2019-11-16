from pages.calendar import *
from selenium.common.exceptions import NoSuchElementException
from datetime import timedelta

def set_create_event_w_attendees(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.add_attendees("dimamail1337@mail.ru")
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