# author: nikola mijovic
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/typos')

assert 'Typos' in driver.find_element(By.CSS_SELECTOR, 'h3').text

sleep(1)

reci = driver.find_element(By.CSS_SELECTOR, 'p:nth-child(3)').text.split(' ')

assert 'won,t' or "won't." in reci[-1]

sleep(1)

driver.refresh()

tekst = driver.find_element(By.CSS_SELECTOR, 'p:nth-child(3)').text

reci = tekst.split(' ')

assert 'won,t' or "won't." in reci[-1]

sleep(1)

driver.minimize_window()

driver.quit()
