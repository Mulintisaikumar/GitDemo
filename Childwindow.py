from selenium import webdriver
from selenium.webdriver.chrome.service import Service



#from SampleProject.POMDdemo.tests.login import driver
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
childwindow = driver.window_handles[1]

driver.switch_to.window(childwindow)

driver.switch_to.window(driver.window_handles[2])

print(driver.find_element_by_tag_name("h3").text)
driver.close()
assert "Open New Window" == driver.find_element_by_tag_name("h3").text
