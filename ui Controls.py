from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path = "C:\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(checkboxes)
checkboxes = len("option2")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
           checkbox.click()
           assert  checkbox.is_selected()
radiobuttons = driver.find_element_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

 #print(driver.find_element_by_id("displayed-text").is_displayed())
#driver.find_element_by_id("hide-textbox").click()
