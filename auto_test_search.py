# author: nikola mijovic

from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://www.google.com/')
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('Python')
search_input.send_keys(Keys.ENTER)
sleep(3)
main_result = driver.find_element(By.XPATH, "//h3[contains(.,'Welcome to Python.org')]")
assert main_result.is_displayed()

driver.get('https://duckduckgo.com/')
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('Python')
search_input.send_keys(Keys.ENTER)
sleep(3)
main_result = driver.find_element(By.XPATH, "//h2[contains(.,'Welcome to Python.org')]")
assert main_result.is_displayed()

driver.get('https://www.bing.com/')
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('Python')
search_input.send_keys(Keys.ENTER)
sleep(3)
main_result = driver.find_element(By.XPATH, "//h2[contains(.,'Welcome to Python.org')]")
assert main_result.is_displayed()

driver.minimize_window()

driver.quit()
