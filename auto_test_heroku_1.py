# author : nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

sleep(2)

driver.find_element(By.CSS_SELECTOR, 'h3')

driver.find_element(By.CSS_SELECTOR, 'button')

driver.find_element(By.CSS_SELECTOR, 'button').click()

sleep(2)

driver.find_element(By.CSS_SELECTOR, '.added-manually')

driver.find_element(By.CSS_SELECTOR, '.added-manually').click()

sleep(2)

driver.minimize_window()

driver.quit()
