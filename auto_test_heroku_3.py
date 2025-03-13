# author: nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/forgot_password')

assert 'Forgot Password' in driver.find_element(By.CSS_SELECTOR, 'h2').text

assert 'E-mail' in driver.find_element(By.CSS_SELECTOR, 'label').text

sleep(1)

driver.find_element(By.ID, 'email').send_keys('nikola.mijovic@gmail.com')

sleep(1)

driver.find_element(By.ID, 'form_submit').click()

sleep(2)

assert 'Internal Server Error' in driver.find_element(By.CSS_SELECTOR, 'h1').text

driver.minimize_window()

driver.quit()
