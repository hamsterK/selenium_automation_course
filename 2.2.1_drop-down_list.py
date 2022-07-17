import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    math_result = int(num1.text) + int(num2.text)
    math_result = str(math_result)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(math_result)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
finally:
    time.sleep(5)
    browser.quit()
