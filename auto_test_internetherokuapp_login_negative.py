# author: nikola mijovic

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/login')
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.CSS_SELECTOR, '.fa')
username_input.send_keys('tomsmith')
password_input.send_keys('abc123')
login_button.click()
sleep(2)
loggin_message = driver.find_element(By.ID, 'flash').text

assert 'Your password is invalid\n×' in loggin_message

driver.get('https://the-internet.herokuapp.com/login')
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.CSS_SELECTOR, '.fa')
username_input.send_keys('tomsmith123')
password_input.send_keys('SuperSecretPassword!')
login_button.click()
sleep(2)
loggin_message = driver.find_element(By.ID, 'flash').text

assert 'Your username is invalid\n×' in loggin_message

driver.minimize_window()

driver.quit()
