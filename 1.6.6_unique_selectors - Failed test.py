from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    numbers = ['first', 'second', 'third']
    for num in numbers:
        field = browser.find_element(By.CSS_SELECTOR, f'.form-control.{num}:required')
        field.send_keys('answer')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(5)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert welcome_text == 'Congratulations! You have successfully registered!'

finally:
    time.sleep(5)
    browser.quit()
