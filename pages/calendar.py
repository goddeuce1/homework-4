from default import *
import datetime
from selenium.webdriver.common.keys import Keys

class CalendarPage(Page):
    PATH = ''

    @property
    def form(self):
        return CalendarForm(self.driver)


class CalendarForm(Component, Page):

    EVENT_PAGE = '//div[@class="event-page"]'
    CREATE_EVENT__BUTTON = '//a[contains(@class, "button_create-event")]'
    SAVE_EVENT__BUTTON = '//a[contains(@class, "event-new__button_submit")]'
    CANCEL_EVENT__BUTTON = '//a[contains(@class, "event-new__reset")]'
    ATTENDEES___INPUT = '//div[@class="attendees-selector__textbox"]//input[@name="input"]'
    EVENT_NAME__INPUT = '//div[@class="event-new__summary event-new__row"]//input'
    DATE_END__INPUT = '//input[@name="dateEnd"]'
    DATE_FORMAT = "%d.%m.%Y"
    LOCATION__INPUT = '//div[@class="event-new__row event-new__row_location"]//input'
    DESCRIPTION__INPUT = '//div[@class="event-new__row event-new__row_description"]//textarea'

    def save_event(self):
        self.wait_for_clickable(self.SAVE_EVENT__BUTTON).click()

    def create_event(self):
        self.wait_for_clickable(self.CREATE_EVENT__BUTTON).click()

    def cancel_event(self):
        self.wait_for_clickable(self.CANCEL_EVENT__BUTTON).click()   

    def set_name(self, name):
        self.wait_for_clickable(self.EVENT_NAME__INPUT).send_keys(name)

    def set_location(self, location):
        self.wait_for_clickable(self.LOCATION__INPUT).send_keys(location)

    def set_description(self, description):
        self.wait_for_clickable(self.DESCRIPTION__INPUT).send_keys(description) 

    def add_attendees(self, email):
        elem = self.wait_for_element(self.ATTENDEES___INPUT)
        elem.send_keys(email)
        elem.send_keys(Keys.ENTER)

    def get_date_end(self):
        elem = self.wait_for_element(self.DATE_END__INPUT)
        dateStr = elem.get_attribute("value")
        return datetime.datetime.strptime(dateStr, self.DATE_FORMAT).date()

    def set_date_end(self, date):
        elem = self.wait_for_element(self.DATE_END__INPUT)
        self.driver.execute_script("arguments[0].setAttribute('value','"+date.strftime(self.DATE_FORMAT)+"')", elem)
        elem.click()

    SETTINGS = '//div[@data-role="popup"]'
    SETTINGS_BUTTON = '//a[@href="?action=settings"]'
    SETTINGS_SUBMIT = '//button[@data-action="submit"]'
    SETTINGS_REMINDERS_BUTTON = '//a[@data-page-link="reminders"]'
    SELECT_CALENDAR = '//select[@data-element="calendar"]'
    SELECT_CALENDAR_ELEMENT = '//option[@value="B4AADE80-1122-42EB-A010-6E7C73804192"]'
    WORKDAY_START = '//input[@name="start"]'
    WORKDAY_END = '//input[@name="end"]'
    WORKDAY_CHECKBOXES = './/span[@class="workdays__day"]'
    WORKDAY_CHECKBOX_ITEM = './/span[@data-id="%d"]'
    WORKDAY_CHECKBOX_ITEM_VALUE = './/input[@class="checkbox-input"]'
    WORKDAY_CHECKBOX_ERROR = '//span[@class="checkbox checkbox_layout_inline checkbox_top checkbox_error"]'
    REMINDERS = '//div[@class="reminders reminders_default"]'
    REMINDERS_ITEM = './/div[@class="reminders-item valign_20"]'
    REMINDERS_ITEM_CHECKBOX = './/span[@data-role="checkbox"]'
    REMINDERS_ITEM_CHECKBOX_EMAIL = './/span[@name="email"]'
    REMINDERS_SOUND = '//span[@name="disable_sound"]'
    REMINDERS_EMAIL_DIV = '//div[@class="form-param__value"]'
    REMINDERS_EMAIL_ITEM = './/div[@class="settings-notify-types-item"]'
    REMINDERS_EMAIL_ITEM_CHECKBOX = './/span[@data-role="checkbox"]'

    def settings_click(self):
        self.wait_for_element(self.SETTINGS_BUTTON)
        self.wait_for_clickable(self.SETTINGS_BUTTON)
        self.driver.find_element_by_xpath(self.SETTINGS_BUTTON).click()

    def settings_submit(self):
        self.wait_for_element(self.SETTINGS_SUBMIT)
        self.wait_for_clickable(self.SETTINGS_SUBMIT)
        self.driver.find_element_by_xpath(self.SETTINGS_SUBMIT).click()

    def change_workday_times(self):
        time_begin = '08:00'
        time_end = '15:00'
        time_format_len = 5

        self.wait_for_element(self.SETTINGS)
        settings = self.driver.find_element_by_xpath(self.SETTINGS)
        self.wait_for_clickable(self.WORKDAY_START)
        start = settings.find_element_by_xpath(self.WORKDAY_START)

        for i in range (0, time_format_len):
            start.send_keys(Keys.BACK_SPACE)

        start.send_keys(time_begin)
        self.wait_for_clickable(self.WORKDAY_END)
        end = settings.find_element_by_xpath(self.WORKDAY_END)

        for i in range (0, time_format_len):
            end.send_keys(Keys.BACK_SPACE)

        end.send_keys(time_end)

    def change_calendar(self):
        self.wait_for_element(self.SETTINGS)
        settings = self.driver.find_element_by_xpath(self.SETTINGS)
        self.wait_for_clickable(self.SELECT_CALENDAR)
        select = settings.find_element_by_xpath(self.SELECT_CALENDAR)
        select.click()

        self.wait_for_clickable(self.SELECT_CALENDAR_ELEMENT)
        select.find_element_by_xpath(self.SELECT_CALENDAR_ELEMENT).click()

    def change_to_two_workdays(self):
        self.wait_for_element(self.SETTINGS)
        settings = self.driver.find_element_by_xpath(self.SETTINGS)
        days = settings.find_elements_by_xpath(self.WORKDAY_CHECKBOXES)

        i = 1
        for item in days:
            self.wait_for_clickable(self.WORKDAY_CHECKBOX_ITEM % i)
            span = item.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM % i)
            value = span.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM_VALUE)
            if value.get_attribute('value') == 'true':
                span.click()
            i += 1

        max_workdays = 2

        i = 1
        for item in days:
            if i <= max_workdays:
                self.wait_for_clickable(self.WORKDAY_CHECKBOX_ITEM % i)
                item.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM % i).click()
                i += 1
            else:
                break

    def change_to_zero_workdays(self):
        self.wait_for_element(self.SETTINGS)
        settings = self.driver.find_element_by_xpath(self.SETTINGS)
        days = settings.find_elements_by_xpath(self.WORKDAY_CHECKBOXES)

        i = 1
        for item in days:
            self.wait_for_clickable(self.WORKDAY_CHECKBOX_ITEM % i)
            span = item.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM % i)
            value = span.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM_VALUE)
            if value.get_attribute('value') == 'true':
                span.click()
            i += 1

    def reminders_click(self):
        self.wait_for_element(self.SETTINGS_REMINDERS_BUTTON)
        self.wait_for_clickable(self.SETTINGS_REMINDERS_BUTTON)
        self.driver.find_element_by_xpath(self.SETTINGS_REMINDERS_BUTTON).click()

    def change_to_one_reminder(self):
        self.wait_for_element(self.REMINDERS)
        reminders = self.driver.find_elements_by_xpath(self.REMINDERS_ITEM)

        for item in reminders:
            self.wait_for_clickable(self.REMINDERS_ITEM_CHECKBOX)
            span = item.find_element_by_xpath(self.REMINDERS_ITEM_CHECKBOX)
            if span.get_attribute('data-checked') == 'true' and span.get_attribute('name') != 'email':
                span.click()
            if span.get_attribute('data-checked') == 'false' and span.get_attribute('name') == 'email':
                span.click()

    def change_to_zero_reminders(self):
        self.wait_for_element(self.REMINDERS)
        reminders = self.driver.find_elements_by_xpath(self.REMINDERS_ITEM)

        for item in reminders:
            self.wait_for_clickable(self.REMINDERS_ITEM_CHECKBOX)
            span = item.find_element_by_xpath(self.REMINDERS_ITEM_CHECKBOX)
            if span.get_attribute('data-checked') == 'true':
                span.click()

    def mute_sound(self):
        self.wait_for_element(self.REMINDERS_SOUND)
        self.wait_for_clickable(self.REMINDERS_SOUND)
        sound = self.driver.find_element_by_xpath(self.REMINDERS_SOUND)
        if sound.get_attribute('data-checked') == 'false':
            sound.click()

    def change_email_reminders(self, state):
        self.wait_for_element(self.REMINDERS_EMAIL_DIV)
        reminders = self.driver.find_elements_by_xpath(self.REMINDERS_EMAIL_ITEM)

        for item in reminders:
            self.wait_for_clickable(self.REMINDERS_EMAIL_ITEM_CHECKBOX)
            span = item.find_element_by_xpath(self.REMINDERS_EMAIL_ITEM_CHECKBOX)
            if span.get_attribute('data-checked') == state:
                span.click()
