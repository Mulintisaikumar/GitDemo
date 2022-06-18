from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

validateText = "Option3"
s = Service("C:\chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name")
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alertText = alert.text
assert validateText in alertText
alert.accept()
