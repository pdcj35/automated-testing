from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://gmail.com")

usuario = driver.find_element("id","identifierId")
usuario.send_keys("pablo.dc35@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(5)

clave = driver.find_element("name","password")
clave.send_keys("PablO1994dcj")
clave.send_keys(Keys.ENTER)
