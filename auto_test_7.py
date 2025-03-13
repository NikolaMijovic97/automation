# author: nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# inicijalizacija Chrome Browsere
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

# maksimizovanje prozora
driver.maximize_window()

# odlazak na URL adresu
driver.get('https://www.selenium.dev/documentation/webdriver/')

# pauza 1 sekunda
sleep(1)

# glavno mesto u testu - verifikacija teksta u browseru titlu
assert 'WebDriver | Selenium' in driver.title

# snimanje screenshota stranice
driver.save_screenshot('webdriver.png')

# minimizovanje prozora
driver.minimize_window()

# pauza 1 sekunda
sleep(1)

# zatvaranje chrome prozora i chrome procesa
driver.quit()
