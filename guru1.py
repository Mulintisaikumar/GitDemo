import random
import time

from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.demo.guru99.com/V4/")

#login
User = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
User.send_keys("mngr409463")

pwd  = driver.find_element(By.CSS_SELECTOR, "input[onkeyup='validatepassword();']")
pwd.send_keys("Urevata")

button = driver.find_element(By.XPATH, "//input[@name='btnLogin']")
button.click()

#Day2
print(driver.title)
print(driver.current_url)
driver.save_screenshot( 'Guru scr#' + str (random.randint(0,77)) + '.png')
