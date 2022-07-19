import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(calc(x.text))

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()

    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()