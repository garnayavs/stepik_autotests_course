from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import log, sin

link = 'https://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    input_answer = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)
    input_answer.send_keys(answer)

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    time.sleep(5)
    browser.quit()
