import time

from  selenium  import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("'https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(4)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item' ] a")
print(countries)
for country in countries:
    if country.text == "india":
        country.click()
        break
print(driver.find_element_by_id("auto-suggest").text)
assert driver.find_element_by_id("auto-suggest").get_attribute('value') == "india"
