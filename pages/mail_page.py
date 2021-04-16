from .base_page import BasePage
from .locators import MailPageLocators


class MailPage(BasePage):
    def should_be_mail_page(self):
        self.should_be_mail_url()
        self.should_be_create_acc_button()

    def should_be_mail_url(self):
        self.url = self.browser.current_url
        assert "account" in self.url, f"'account' isn't present in the url, got {self.url}"

    def should_be_create_acc_button(self):
        button = self.is_element_present(*MailPageLocators.CREATE_ACC_BUTTON)  # проверка, что есть форма логина
        assert button, f"create acc button isn't present on the page, used locator {MailPageLocators.CREATE_ACC_BUTTON}"
