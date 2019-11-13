import urlparse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Page(object):
    BASE_URL = 'https://calendar.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(element)
        )

    def wait_for_disappear(self, element):
        WebDriverWait(self.driver, 5).until_not(
            EC.presence_of_element_located((By.XPATH, element))
        )