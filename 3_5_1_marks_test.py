import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    @pytest.mark.win10
    @pytest.mark.skip # to skip the test, no flags required in terminal
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")  # the test is expected to fail == a known issue
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

        '''
        @pytest.mark.smoke/regression - 
        only these tests will be performed
        
        to launch the test:
        pytest -v 3_5_1_marks_test.py - skip will be used here too
        pytest -rX -v 3_5_1_marks_test.py - show specific info on XFAIL
        pytest -s -v -m smoke 3_5_1_marks_test.py - only smoke test
        pytest -s -v -m "not smoke" 3_5_1_marks_test.py - all test except smoke
        pytest -s -v -m "smoke or regression" 3_5_1_marks_test.py - smoke AND regression
        pytest -s -v -m "smoke and win10" 3_5_1_marks_test.py - only for win10

        
        to avoid warnings 'unknown marks' =>
        create a file pytest.ini => add text:
        
        [pytest]
        markers =
            smoke: marker for smoke tests
            regression: marker for regression tests    
            
        about XFAIL optional parameters:
        https://docs.pytest.org/en/latest/reference/reference.html?highlight=xfail#pytest-mark-xfail   
        '''