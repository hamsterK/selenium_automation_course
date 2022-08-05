from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_present(browser):
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, '.add-to-basket')
    assert len(add_to_basket_button), 'Add to basket button is missing'

# pytest -s -v --language=es 3_6_7_lang_auto_test.py

