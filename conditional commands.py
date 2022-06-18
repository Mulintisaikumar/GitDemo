import links as links
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
links: links() = driver.find_element(By.pag_name,'a')
print(len(links))
for link in links:
    print(link.text)
