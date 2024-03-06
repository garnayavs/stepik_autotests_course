from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

link = 'https://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    trollface_btn = browser.find_element(By.CSS_SELECTOR, '.trollface.btn')
    trollface_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    answer = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)

    submit_btn = browser.find_element(By.CLASS_NAME, 'btn')
    submit_btn.click()

finally:
    print(browser.switch_to.alert.text)
    #time.sleep(15)
    browser.quit()


