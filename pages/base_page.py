from .locators import BasePageLocators
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, browser, url, timeout=10):  #конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
