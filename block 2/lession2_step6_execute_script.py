from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.send_keys(answer)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(15)
    browser.quit()
