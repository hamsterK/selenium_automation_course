import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(calc(x.text))

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
