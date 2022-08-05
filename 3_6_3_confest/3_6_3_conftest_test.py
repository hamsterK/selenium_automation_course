from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

# pytest -s -v 3_6_3_conftest_test.py

# use 'conftest.py to set fixtures to all the files in the directory