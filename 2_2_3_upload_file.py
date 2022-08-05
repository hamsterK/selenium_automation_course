import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys('Мой ответ')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'upload_file.txt'
    file_path = os.path.join(current_dir, file_name)
    upload_button = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    upload_button.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))