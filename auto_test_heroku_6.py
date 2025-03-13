# author: nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/tables')

driver.find_element(By.XPATH, "//span[contains(.,'Last Name')]").click()

sleep(1)

driver.find_element(By.XPATH, "//span[contains(.,'First Name')]").click()

sleep(1)

driver.find_element(By.XPATH, "//span[contains(.,'Email')]").click()

sleep(1)

driver.find_element(By.XPATH, "//span[contains(.,'Due')]").click()

sleep(1)

driver.find_element(By.XPATH, "//span[contains(.,'Web Site')]").click()

sleep(1)

driver.find_element(By.XPATH, "//span[contains(.,'Action')]").click()

sleep(1)

print(driver.find_element(By.CSS_SELECTOR, '#table1 tr:nth-child(1) > td:nth-child(1)').text)

print(driver.find_element(By.CSS_SELECTOR, '#table1 tr:nth-child(1) > td:nth-child(2)').text)

print(driver.find_element(By.CSS_SELECTOR, '#table1 tr:nth-child(1) > td:nth-child(3)').text)

print(driver.find_element(By.CSS_SELECTOR, '#table1 tr:nth-child(1) > td:nth-child(4)').text)

print(driver.find_element(By.CSS_SELECTOR, '#table1 tr:nth-child(1) > td:nth-child(5)').text)

driver.find_element(By.CSS_SELECTOR, '#table1 tr:nth-child(4) a:nth-child(1)').click()

driver.find_element(By.CSS_SELECTOR, '#table1 tr:nth-child(4) a:nth-child(2)').click()

driver.minimize_window()

driver.quit()
