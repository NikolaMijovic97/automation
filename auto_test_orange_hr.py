# author: nikola mijovic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

sleep(2)

username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.CSS_SELECTOR, '.oxd-button')

username_input.send_keys('Admin')
password_input.send_keys('admin123')
login_button.click()

sleep(3)

# hvatanje svih elemnta sa ovom klasom i stavlnaje njih u listu
text_list = driver.find_elements(By.CSS_SELECTOR, '.oxd-text')

# stampanje svih clanova liste(njihovog teksta)
# for i in text_list:
#     print(i.text)

# assertovanje teksta sa osmi clan u listi - Dashborad
assert 'Dashboard' in text_list[7].text

driver.minimize_window()

driver.quit()
