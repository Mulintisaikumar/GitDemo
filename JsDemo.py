#Js Dom can any elements on web page just like how selenium does
#selenium have a method to javascript code in it
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://rahulshettyacademy.com/angularpractice/")
#name
hello = driver.find_element(By.NAME, "name")
hello.send_keys("Sai Kumar")
print(driver.find_element(By.NAME, "name").text)
print(driver.find_element(By.NAME, "name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element(By.CSS_SELECTOR,"a[href*='shop']")
driver.execute_script("arguments[0].click();",shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")