# script to unenroll from all the courses on cms 
# https://chromedriver.chromium.org/downloads download the chrome driver based on the chrome version you are using. 
# make changes to the editable part (as per the instructions mentioned there) and you are good to go. 

from time import sleep 
from selenium import webdriver
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from datetime import datetime,timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

## EDITABLE PART BELOW ##
########################################################
course_lists='''BIO F110 BIOLOGY LABORATORY P Sem 2 2021-22
BIO F110 BIOLOGY LABORATORY P3 Sem 2 2021-22'''                           ## copy all the courses u wanna unenroll from 
email='f20xxyyyy@hyderabad.bits-pilani.ac.in'               ## enter the ur gmail account here 
password='password'                                         ## enter your gmail password here  
path_of_driver='/Users/tejasvichabbra/Desktop/chromedriver' ## path where the driver is installed 
#############################################################

driver=webdriver.Chrome(path_of_driver)

url = "https://cms.bits-hyderabad.ac.in/my/#"  # Opening CMS
driver.get(url)

# Google login for CMS 
result = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/a')))
sleep(1.0)
result.click()
inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
inputElement.send_keys(email)
sleep(0.5)
inputElement.send_keys(Keys.ENTER)
sleep(3.0)
passWordBox = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
passWordBox.send_keys(password)
sleep(0.5)
passWordBox.send_keys(Keys.ENTER)
print("Logged in successfully.")
sleep(10.0)

def bye_bye(course): # unenroller fucntion 
    inputElement = driver.find_element_by_link_text(course)
    inputElement.send_keys(Keys.ENTER)
    sleep(1.5)
    inputElement = driver.find_element_by_id("action-menu-toggle-2")
    inputElement.send_keys(Keys.ENTER)
    sleep(1.5)
    inputElement = driver.find_element_by_partial_link_text('Unenrol me')
    inputElement.send_keys(Keys.ENTER)
    sleep(1.0)
    inputElement = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/section/div/div/div/div[3]/div/div[1]/form/button")
    inputElement.send_keys(Keys.ENTER)

courses=course_lists.splitlines()
for course  in courses:
    bye_bye(course)
    print(course, " unenrolled.")  
    sleep(1.0)
    url = "https://cms.bits-hyderabad.ac.in/my/#"
print("Unenrolled all successfully.")