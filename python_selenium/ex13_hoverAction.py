from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver")
driver.get("https://www.google.com")
time.sleep(1)
elem = driver.find_element("link text","Privacidad")

hover = ActionChains(driver).move_to_element(elem)
hover.perform()
time.sleep(3)