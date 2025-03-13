# author: nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/redirector')

sleep(2)

assert 'Redirection' in driver.find_element(By.CSS_SELECTOR, 'h3').text

driver.find_element(By.ID, 'redirect').click()

sleep(2)

assert 'Status Code' in driver.find_element(By.CSS_SELECTOR, 'h3').text

driver.find_element(By.LINK_TEXT, '200').click()

driver.back()

sleep(3)

driver.find_element(By.LINK_TEXT, 'here').click()

assert 'Hypertext Transfer Protocol' in driver.find_element(By.CSS_SELECTOR, 'h1').text

driver.minimize_window()

driver.quit()
