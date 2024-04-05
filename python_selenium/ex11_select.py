import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class use_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_select(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
		selec = driver.find_element("xpath","//*[@id='main']/div[3]/div[1]/select")
		opcion = selec.find_elements("tag name","option")
		for option in opcion:
			print("Los valores son: %s" % option.get_attribute("value"))
			option.click()
			time.sleep(1)
		seleccionar = Select(driver.find_element("xpath","//*[@id='main']/div[3]/div[1]/select"))
		seleccionar.select_by_value("10")
		time.sleep(3)

if __name__ == '__main__':
	unittest.main()