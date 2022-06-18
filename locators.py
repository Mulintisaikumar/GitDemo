import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("sai")
driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[1]/input").send_keys('SAI')
driver.find_element_by_name("email").send_keys("KUMAR")

driver.find_element_by_id("exampleCheck1").click()
#selectclass provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
dropdown.select_by_visible_text(1)
time.sleep(5)
dropdown.select_by_visible_text(0)

driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_name("alert-success").text
assert "success" in message
#[contains(@class'alert-success')] - xpath
#[calss*='alert-success']   -css