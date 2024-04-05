from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com")
time.sleep(1)
encontrar = driver.find_element("link text","Learn PHP")
encontrar.click()
time.sleep(3)

driver.close()