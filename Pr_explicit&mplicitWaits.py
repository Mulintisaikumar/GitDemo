from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div[1]/div[3]/button").click()
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div[2]/div[3]/button").click()
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div[3]/div[3]/button").click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[3]/div[2]/div[2]/button").click()
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("Saikumar")


