from default import *
import datetime

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

