# author: nikola mijovic

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.get('https://www.saucedemo.com/v1/index.html')
driver.minimize_window()
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')
username_input.send_keys('locked_out_user')
password_input.send_keys('secret_sauce')
login_button.click()
sleep(3)
error_message = driver.find_element(By.CSS_SELECTOR, '.error-button')
assert error_message.is_displayed()

driver.get('https://www.saucedemo.com/v1/index.html')
driver.minimize_window()
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')
username_input.send_keys('fake-user')
password_input.send_keys('fake-password')
login_button.click()
sleep(3)
error_message = driver.find_element(By.CSS_SELECTOR, '.error-button')
assert error_message.is_displayed()

driver.minimize_window()

driver.quit()
