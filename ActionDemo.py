from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\chromedriver")
driver = webdriver.Chrome(service=s)

#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#action = ActionChains(driver)
#menu = driver.find_element_by_id("mousehover")

#action.move_to_element(menu).perform()
#childmenu = driver.find_element_by_link_text("Reload")
#action.move_to_element("childmenu").click().perform()


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)

action.context_click(driver.find_element(By.ID,"double-click")).perform()
action.double_click(driver.find_element(By.ID,"double-click")).perform()

#alert button
alert = driver.switch_to.alert
assert "you double clicked me ! ! !, you got to be kidding me" == alert.text()
alert.accept()

print(driver.find_element_by_id("displayed-text").is_displayed())
driver.find_element_by_id("hide-textbox").click()
