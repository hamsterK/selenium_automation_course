from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

# use terminal to see 'print' outputs: pytest -s 3_4_1_fixture1_test.py


class TestMainPage1:
    # browser opened once for all tests, then closed after all tests

    @classmethod
    def setup_class(cls):
        """ setup any state tied to the execution of the given method in a
          class.  setup_method is invoked for every test method of a class.
          """
        print("\nstart browser for test suite..")
        cls.browser = webdriver.Chrome()

    # noinspection PyUnresolvedReferences
    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a setup_method
            call.
            """
        print("quit browser for test suite..")
        cls.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2:
    # browser opened and closed for each test separately

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")