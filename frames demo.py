from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service (executable_path="C:\\chromedriver.exe")
#iframe, frameset, frame
driver = webdriver.Chrome(service = s)


driver.get("https://the-internet.herokuapp.com/iframe")
#frame id  or  frame name   or index  value
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys(" I'M able to automated SoftWare ")
driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)

