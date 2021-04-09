import time
from .pages.main_page import MainPage
import pytest

# pytest -v --tb=line --language=en test_main_page.py::test_guest_cant_see_product_in_basket_opened_from_main_page
# pytest -v --tb=line --language=en -m login_guest test_main_page.py

url = "http://mail.ru/"



@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, url)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                             # открываем страницу
        time.sleep(10)
