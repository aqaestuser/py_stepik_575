import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button_book = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button_book.click()

    x_value = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x_value))

    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()
