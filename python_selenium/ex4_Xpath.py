import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class use_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_buscar_por_xpath(self):
		# xpath es una estructura de objetos → relativo, absoluto
		# retalivo → busca a partir del nodo, en cualquier carpeta de la ruta
		# absoluto → busca en la dirección específica
		driver = self.driver
		driver.get("https://www.demoblaze.com/")
		time.sleep(5)
		buscar = driver.find_element("xpath","//*[@id='tbodyid']/div[1]/div/div/h4/a")
		time.sleep(5)
		buscar.click()
		time.sleep(5)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()