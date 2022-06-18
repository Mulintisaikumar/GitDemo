from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://www.google.com/search?q=internet+herokuapp&sxsrf=ALiCzsaJ_4zVR0f8e0IOLIB7mk9-1Bm-2g%3A1652435478324&source=hp&ei=Fip-Yv3iEcGA-Aba_aPQBg&iflsig=AJiK0e8AAAAAYn44JilTqfHOnEdU_jX9PTRT1bV9Vfis&ved=0ahUKEwj9xcrtmdz3AhVBAN4KHdr-CGoQ4dUDCAc&uact=5&oq=internet+herokuapp&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCCMQ6gIQJzoECCMQJ1CEQliEQmCUzwxoAnAAeACAAXGIAd4BkgEDMC4ymAEAoAECoAEBsAEK&sclient=gws-wiz")
driver.maximize_window()
driver.find_element_by_css_selector("a[href='https://the-internet.herokuapp.com/windows']").click()
driver.find_element_by_xpath("//a[@target='_blank']").click()
child_window = driver.window_handles[1]
print(driver.find_element_by_xpath("//a[@target='_blank']"))
driver.close()

