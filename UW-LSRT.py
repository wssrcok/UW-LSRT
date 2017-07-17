from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(netID, password):

	browser.get("https://weblogin.washington.edu/")

	netIDbox = browser.find_element_by_id("weblogin_netid")
	netIDbox.send_keys(netID)

	passwordBox = browser.find_element_by_id("weblogin_password")
	passwordBox.send_keys(password)

	submit = browser.find_element_by_name("submit")
	submit.click()

def get_status(sln):
	status = ''
	browser.get("https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=AUT+2017&SLN=" + sln)
	print("analyzing course status")
	time.sleep(10) # make sure give it long enough time to load page
	while status != "Open":    # keep refreshing the status page
		browser.get("https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=AUT+2017&SLN=" + sln)
		time.sleep(1) #give it 1 sec to load (maybe trivial)
		elem = browser.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[5]/tt/b")
		status = str(elem.text)
	# status is Open once get out of the while loop

# main block 
netID = raw_input("Enter your NetID: ")
password = raw_input("Enter your Password: ")

browser = webdriver.Chrome()
login(netID, password)
sln = raw_input("what's the SLN of your course? ")
get_status(sln)
# now the course should be open
browser.get("""https://sdb.admin.uw.edu/students/UWNetID/register.asp?INPUTFORM=UPDATE&PAC=0&M
				AXDROPS=0&_CW=a6e08bbc05bff14c8d57bb0e220bbafeeff6b1dbc18afe22fc8a07dd3d02e4b8
				&QTR=4&YR=2017
				&sln1=""" + sln + "&entcode1=&credits1=&gr_sys1=")
# 
# need to check if it's really updated. if not, go back and start over.
#

close = raw_input("close the browser? (enter to quit) ")
while (close != ''):
	close = raw_input("close the browser? (enter to quit) ")
browser.close()

