from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path = "C:\\chromedriver.exe")
#driver_service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
#driver=webdriver.Ie(executable_path="C:\\IEDriverServer.exe")

driver.get("https://rahulshettyacademy.com/#/index") # get methid
print(driver.title)
print(driver.current_url)
driver.get("https://www.python.org/")
driver.back()
driver.refresh()
driver.close()