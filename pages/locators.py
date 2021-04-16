from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "a.resplash-btn")
    MAIL_LINK = (By.CSS_SELECTOR, ".svelte-1a5kxdz:nth-child(2)")
    # BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    # USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MailPageLocators():
    CREATE_ACC_BUTTON = (By.CSS_SELECTOR, "signup-link")
