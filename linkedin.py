from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag


url = "http://linkedin.com/"

network_url = "http://linkedin.com / mynetwork/"

driver = webdriver.Chrome('C:\\Program Files\\Web Driver\\chromedriver.exe')	
driver.get(url)


username = driver.find_element_by_id("login-email")

username.send_keys("username")

password = driver.find_element_by_id("login-password")

password.send_keys("password")	

driver.find_element_by_id("login-submit").click()		

driver.find_element_by_id("mynetwork-tab-icon").click()

n = input("Number of requests: ")

for i in range(0, n):
	pag.click(880, 770)
print("Done !")

