from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("file:///C:/Users/pablo/Documents/PDCJ/python_selenium/alert_simple.html")
time.sleep(1)
alerta_simple = driver.find_element("name","alert")
alerta_simple.click()
time.sleep(5)
alerta_simple = driver.switch_to.alert
alerta_simple.dismiss()
time.sleep(3)

driver.close()