# author: nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/checkboxes')

assert 'Checkboxes' in driver.find_element(By.CSS_SELECTOR, 'h3').text

assert 'checkbox 1\ncheckbox 2'in driver.find_element(By.ID, 'checkboxes').text

driver.find_element(By.CSS_SELECTOR, 'input:nth-child(3)').click()

sleep(3)

driver.find_element(By.CSS_SELECTOR, 'input:nth-child(3)').click()

sleep(3)

driver.find_element(By.CSS_SELECTOR, 'input:nth-child(3)').click()

sleep(3)

driver.minimize_window()

driver.quit()
