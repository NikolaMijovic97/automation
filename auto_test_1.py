# author: nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://www.bing.com')

sleep(1)

print(driver.title)

print(driver.current_url)

driver.save_screenshot('bing.png')

driver.minimize_window()

sleep(1)

driver.quit()
