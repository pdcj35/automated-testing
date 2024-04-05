from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/default.asp")
content = driver.find_element("css selector","a.w3-btn")
content.click()
time.sleep(5)

driver.close()