from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/registration1.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    fields = browser.find_elements(By.CSS_SELECTOR, ':required')
    for field in fields:
        field.send_keys('answer')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(5)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(5)
    browser.quit()
