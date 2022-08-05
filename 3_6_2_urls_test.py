import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_links(browser, url):
    link = f'https://stepik.org/lesson/{url}/step/1'
    browser.get(link)
    text_field = browser.find_element(By.CSS_SELECTOR, 'textarea')
    answer = math.log(int(time.time()))
    text_field.send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']").click()
    answer_message = browser.find_element(By.CSS_SELECTOR, '.smart-hints').text
    assert answer_message == 'Correct!', 'Text != Correct!'

# pytest -s -v 3_6_2_urls_test.py