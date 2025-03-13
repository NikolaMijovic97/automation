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

username_input.send_keys('standard_user')

password_input.send_keys('secret_sauce')

login_button.click()

sleep(2)

burger_icon = driver.find_element(By.CSS_SELECTOR, '.bm-burger-button')

burger_icon.click()

sleep(2)

logout_link = driver.find_element(By.ID, 'logout_sidebar_link')

logout_link.click()

driver.refresh()

username_input.send_keys(' ')

password_input.send_keys(' ')

login_button.click()

sleep(2)

error_message = driver.find_element(By.CSS_SELECTOR, 'error-button')

sleep(2)

driver.minimize_window()

driver.quit()
