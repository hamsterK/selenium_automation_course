from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRequiredFields(unittest.TestCase):
    def test_first(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        field = browser.find_element(By.CSS_SELECTOR, '.form-control.first:required')
        field.send_keys('answer')
        field = browser.find_element(By.CSS_SELECTOR, '.form-control.second:required')
        field.send_keys('answer')
        field = browser.find_element(By.CSS_SELECTOR, '.form-control.third:required')
        field.send_keys('answer')
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = 'Congratulations! You have successfully registered!'
        self.assertEqual(welcome_text, welcome_text_elt.text)
        time.sleep(5)
        browser.quit()

    def test_second(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        field = browser.find_element(By.CSS_SELECTOR, '.form-control.first:required')
        field.send_keys('answer')
        field = browser.find_element(By.CSS_SELECTOR, '.form-control.second:required')
        field.send_keys('answer')
        field = browser.find_element(By.CSS_SELECTOR, '.form-control.third:required')
        field.send_keys('answer')
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = 'Congratulations! You have successfully registered!'
        self.assertEqual(welcome_text, welcome_text_elt.text)
        time.sleep(5)
        browser.quit()



if __name__ == "__main__":
    unittest.main()
