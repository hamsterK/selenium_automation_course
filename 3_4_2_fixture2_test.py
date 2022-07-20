import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture  # fixture will be a parameter in tests below, default scope='function'
#@pytest.fixture(scope='class')
def browser():
    print('\nstart browser for test...')
    browser = webdriver.Chrome()
    yield browser
    # the following code will be executed at the end of the test
    print('\nquit browser...')
    browser.quit()


class TestMainPage1:
    def test_guest_should_see_login_link(self, browser):  # browser == fixture
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')


'''@pytest.fixture(scope='function', autouse=False) - default
scope='function'/'class'/'module'/session
fixture is applied to every function/class/etc

autouse=False => fixture needs to be called manually ,
if True - will be aaplied automatically according to the 'scope'
'''