from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webpage = "https://weblogin.washington.edu/" # edit me
netID = "wssrcok"
password = "Src052012"

driver = webdriver.Chrome()
driver.get(webpage)

netIDbox = driver.find_element_by_id("weblogin_netid")
netIDbox.send_keys(netID)

passwordBox = driver.find_element_by_id("weblogin_password")
passwordBox.send_keys(password)


submit = driver.find_element_by_name("submit")
submit.click()