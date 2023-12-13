from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    item = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert item, "button 'Add to basket' not found"