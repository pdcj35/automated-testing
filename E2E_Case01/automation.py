import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

delay = 3
driver = webdriver.Chrome()

# Enter WebSite

driver.get("https://www.demoblaze.com/")
time.sleep(delay)
driver.save_screenshot('01_WebSite.png')

# Add items to cart

item1 = driver.find_element("xpath","//*[@id='tbodyid']/div[1]/div/div/h4/a")
item1.click()
time.sleep(delay)

add_item1 = driver.find_element("xpath","//*//*[@id='tbodyid']/div[2]/div/a")
add_item1.click()
time.sleep(delay)

alert = driver.switch_to.alert
alert.dismiss()
time.sleep(delay)

driver.save_screenshot('02_Item1Added.png')

back_home = driver.find_element("xpath","//*[@id='navbarExample']/ul/li[1]/a")
back_home.click()
time.sleep(delay)

item2 = driver.find_element("xpath","//*[@id='tbodyid']/div[2]/div/div/h4/a")
item2.click()
time.sleep(delay)

add_item2 = driver.find_element("xpath","//*[@id='tbodyid']/div[2]/div/a")
add_item2.click()
time.sleep(delay)

alert = driver.switch_to.alert
alert.dismiss()
time.sleep(delay)

driver.save_screenshot('03_Item2Added.png')

# Enter cart

cart_in = driver.find_element("xpath","//*[@id='cartur']")
cart_in.click()
time.sleep(delay)

driver.save_screenshot('04_CartVisualized.png')

place_order = driver.find_element("xpath","//*[@id='page-wrapper']/div/div[2]/button")
place_order.click()
time.sleep(delay)

# Purchase before complete the form

purchase_noform = driver.find_element("xpath","//*[@id='orderModal']/div/div/div[3]/button[2]")
purchase_noform.click()
time.sleep(delay)

alert = driver.switch_to.alert
alert.dismiss()
time.sleep(delay)

# Complete form

name_form = driver.find_element("xpath","//*[@id='name']")
name_form.send_keys("TestName")

country_form = driver.find_element("xpath","//*[@id='country']")
country_form.send_keys("TestCountry")

city_form = driver.find_element("xpath","//*[@id='city']")
city_form.send_keys("TestCity")

cc_form = driver.find_element("xpath","//*[@id='card']")
cc_form.send_keys("00000")

month_form = driver.find_element("xpath","//*[@id='month']")
month_form.send_keys("TestMonth")

year_form = driver.find_element("xpath","//*[@id='year']")
year_form.send_keys("2023")

driver.save_screenshot('05_FormCompleted.png')

time.sleep(delay)

# Purchase done

purchase = driver.find_element("xpath","//*[@id='orderModal']/div/div/div[3]/button[2]")
purchase.click()
time.sleep(delay)

driver.save_screenshot('06_PurchaseDone.png')

finished = driver.find_element("xpath","/html/body/div[10]/div[7]/div/button")
finished.click()
time.sleep(delay)
