import time
from pages.main_page import MainPage
from pages.mail_page import MailPage
import pytest

# pytest -v --tb=line --language=en test_main_page.py::TestLoginFromMainPage
# pytest -v --tb=line --language=en --browser_name=chrome -m login_guest test_main_page.py

url = "http://mail.ru/"


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, url)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                            # открываем страницу
        page.should_be_login_link()
        time.sleep(5)
        page.go_to_mail_page()           # выполняем метод страницы — переходим на страницу почты
        mail = MailPage(browser, browser.current_url)  # Инициализируем LoginPage в теле теста
        mail.should_be_mail_page()
        time.sleep(5)
