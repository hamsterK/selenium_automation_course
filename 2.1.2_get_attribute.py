import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    chest = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = chest.get_attribute('valuex')
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(calc(x))

    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()





