from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag


url = "http://linkedin.com/"

network_url = "http://linkedin.com / mynetwork/"

driver = webdriver.Chrome('C:\\Program Files\\Web Driver\\chromedriver.exe')	
driver.get(url)


user = driver.find_element_by_id("login-email")

user.send_keys("username")

passs = driver.find_element_by_id("login-password")

passs.send_keys("password")	

driver.find_element_by_id("login-submit").click()		

driver.find_element_by_id("mynetwork-tab-icon").click()

n = input("Enter number of requests: ")

for i in range(0, n):
	pag.click(880, 770)
print("Done !")

