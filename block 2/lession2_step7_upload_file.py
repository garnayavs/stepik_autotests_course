from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'https://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input_firstname.send_keys('PEPE')
    input_lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input_lastname.send_keys('FROG')
    input_email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input_email.send_keys('pepe@frog.ru')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'pepega.txt')
    # прикрепляем файл
    upload_button = browser.find_element(By.ID, 'file')
    upload_button.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()

finally:
     time.sleep(15)
     browser.quit()
     