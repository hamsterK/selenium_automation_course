import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--languages', action='store', default='en', help='Choose your language')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('languages')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser...')
    time.sleep(10)
    browser.quit()

'''
for firefox:
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
'''