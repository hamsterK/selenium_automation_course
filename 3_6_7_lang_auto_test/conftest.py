import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose your language')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    link = f'http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/'
    browser.get(link)
    yield browser
    time.sleep(30)
    print('\nquit browser...')
    browser.quit()
