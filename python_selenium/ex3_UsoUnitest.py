import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")


	def test_buscar(self):
		driver = self.driver
		driver.get("http://www.google.com")
		self.assertIn("Google", driver.title)
		elemento = driver.find_element("name","q")
		elemento.send_keys("selenium")
		elemento.send_keys(Keys.RETURN)
		time.sleep(5)
		assert "No se encontró" not in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__=='__main__':
	unittest.main()