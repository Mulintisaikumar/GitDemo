from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("------start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("---ignore-certificate-errors")

s = Service("C:\\chromedriver.exe")
driver=webdriver.Chrome(service = s)


driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

