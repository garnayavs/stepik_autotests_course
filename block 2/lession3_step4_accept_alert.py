from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    answer = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()
