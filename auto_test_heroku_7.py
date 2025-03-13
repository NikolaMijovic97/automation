# author: nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/tables')

sleep(1)

a = 1
while a < 5:
    lokator = '#table1 tr:nth-child(' + str(a) + ') > td:nth-child(1)'
    print(driver.find_element(By.CSS_SELECTOR, lokator).text)
    a = a + 1

a = 1
while a < 5:
    lokator = '#table1 tr:nth-child(' + str(a) + ') > td:nth-child(3)'
    print(driver.find_element(By.CSS_SELECTOR, lokator).text)
    a = a + 1

websites = []
a = 1
while a < 5:
    lokator = '#table1 tr:nth-child(' + str(a) + ') > td:nth-child(5)'
    websites.append(driver.find_element(By.CSS_SELECTOR, lokator).text)
    a = a + 1

print(websites)

driver.minimize_window()

driver.quit()
