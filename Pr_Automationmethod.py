from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//input[@id='checkBoxOption2']").click()
driver.find_element_by_xpath("//input[@id='checkBoxOption3']").click()
driver.find_element_by_xpath("//input[@placeholder='Enter Your Name']").send_keys("Sai Kumar")
driver.find_element_by_xpath("//input[@onclick='displayConfirm()']").click()

#driver.find_element_by_xpath("//*[@id='openwindow']").click()

