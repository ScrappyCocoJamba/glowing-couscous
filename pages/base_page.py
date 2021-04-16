from .locators import BasePageLocators
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, browser, url, timeout=10):  #конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_mail_page(self):
        link = self.browser.find_element(*BasePageLocators.MAIL_LINK)
        link.click()

    def is_element_present(self, how, what):
        # Чтобы перехватывать исключение, нужна конструкция try/except
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):                             #открывает нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
