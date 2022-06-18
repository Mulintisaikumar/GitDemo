import random
import time

from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://tutorialsninja.com/demo/")
driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[6]/a")
#iPhoneclick()
iPhones = driver.find_element(By.XPATH, "//a[text()='iPhone']")
iPhones.click()
print(driver.find_element(By.XPATH, "//a[text()='iPhone']"))
#iPhone img view
img = driver.find_element(By.CSS_SELECTOR, "img[alt='iPhone']")
img.click()
#next click()
next_click = driver.find_element(By.XPATH, "/html/body/div[2]/div/button[2]")
for i in range(0,5):
    next_click.click()
    time.sleep(2)
driver.save_screenshot( 'screenshot#' + str (random.randint(0,77)) + '.png')
exit_button = driver.find_element(By.XPATH, "//button[@title='Close (Esc)']")
exit_button.click()
time.sleep(2)
quantity = driver.find_element(By.ID,"input-quantity")
quantity.click()
quantity.clear()
quantity.send_keys(2)
time.sleep(2)
driver.find_element(By.ID, "button-cart").click()
driver.find_element(By.CSS_SELECTOR," #cart-total").click()
laptops = driver.find_element(By.XPATH, "//a[text()='Laptops & Notebooks']")
laptops.click()
time.sleep(2)
#laptops = driver.find_element_by_xpath("//a[text()='show All Laptops & Notebooks']")
#action =ActionChains(laptops)
#action.move_to_element(laptops).perform()
#time.sleep(2)
#driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[2]/div/a").click()
#time.sleep(2)
#laptops_2 = driver.find_element_by_xpath("//a[text()='show All Laptops & Notebooks']")
driver.find_element(By.XPATH, "//a[text()='Show All Laptops & Notebooks']").click()
HP_select = driver.find_element(By.XPATH, "//*[@id='content']/div[4]/div[2]/div/div[2]/div[1]/h4/a")
HP_select.click()
# add hp lap
add_to_button_2 = driver.find_element(By.ID, "button-cart")
add_to_button_2.click()
time.sleep(2)
# calender
calender = driver.find_element(By.XPATH, "//*[@id='product']/div[1]/div/span/button/i")
calender.click()
time.sleep(2)

next_click.calender = driver.find_element(By.XPATH, "//th[@class='next']")

#select month
month_year = driver.find_element(By.XPATH, "//th[@class='picker-switch']")
while month_year == 'December 2022':
    next_click.calender.click()
time.sleep(2)

#select day
calender_date = driver.find_element(By.XPATH, "//td[text()='31']")
calender_date.click()
time.sleep(2)

add_to_button_2.clear()

#checkout
go_to_cart = driver.find_element(By.ID,"cart-total")
go_to_cart.click()

#checkout right click
checkout = driver.find_element(By.XPATH, "//*[@id='cart']/ul/li[2]/div/p/a[2]/strong")
checkout.click()
time.sleep(1)

#click Button
radio_button = driver.find_element(By.CSS_SELECTOR, "input[value='guest']")
radio_button.click()

