import subprocess
import sys
from termcolor import colored
try:
	from selenium import webdriver
except:
	print ("selenium not installed")
	print ('Installing!!!!')
	subprocess.call([sys.executable, '-m', 'pip', 'install','selenium'] )
try:
	import pyfiglet
except:
	print ('pyfiglet not installed')
	print ('Installing')
	subprocess.call([sys.executable, '-m', 'pip3', 'install','pyfiglet'] )	
import time
banner1 = pyfiglet.figlet_format("Welcome!!")
print (colored(banner1,'red'))
print (colored('credits to r4gesingh47','yellow'))
userinput=input(colored('Enter the Amizone user id : ','red'))
passinput=input(colored('Enter the Amizone password : ','red'))
tableday=input(colored('Enter the Day ex Monday: ','red'))
print ('starting process!!!!')
browser=webdriver.Firefox()
browser.maximize_window()
time.sleep(5)
browser.get('https://student.amizone.net/')
user=browser.find_element_by_css_selector('#loginform > div:nth-child(2) > input:nth-child(1)')
user.click()
user.send_keys(userinput)
passw=browser.find_element_by_css_selector('div.validate-input:nth-child(3) > input:nth-child(1)')
passw.click()
passw.send_keys(passinput)
login=browser.find_element_by_css_selector('div.container-login100-form-btn:nth-child(5) > button:nth-child(1)')
login.click()
time.sleep(5)
table=browser.find_element_by_xpath('//*[@id="10"]')
table.click()
time.sleep(4)
if tableday=='Monday':
	i=2
elif tableday=='Tuesday':
	i=3
elif tableday=='Wednesday':
	i=4
elif tableday=='Thursday':
	i=5
elif tableday=='Friday':
	i=6
elif tableday=='Saturday':
	i=7
elif tableday=='Sunday':
	i=1
day=browser.find_element_by_css_selector('#myTab3 > li:nth-child(%s) > a:nth-child(1)'%(i))
day.click()
has='#'
dayid=has+tableday
content=browser.find_element_by_css_selector(dayid)
store=open('timetabledata.txt','a')
store.write(content.text)
print ('*' * 50)
print (r'TIME TABLE HAS BEEN WRITTEN IN timetabledata.txt')
