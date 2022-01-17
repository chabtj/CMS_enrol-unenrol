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
course_lists='''BIO F110 BIOLOGY LABORATORY P
BIO F110 BIOLOGY LABORATORY P3'''                           ## copy all the courses u wanna unenroll from 
email='f20xxyyyy@hyderabad.bits-pilani.ac.in'               ## enter the ur gmail account here 
password='password'                                         ## enter your gmail password here  
path_of_driver='/Users/tejasvichabbra/Desktop/chromedriver' ## path where the driver is installed 
semester='Second Semester 2021-2022'                        ## Sem in which the course is offered 
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

def hi(course): # unenroller fucntion 
    inputElement = driver.find_element_by_partial_link_text('All courses')
    inputElement.send_keys(Keys.ENTER)
    sleep(1.0)
    inputElement = driver.find_element_by_partial_link_text(semester)
    inputElement.send_keys(Keys.ENTER)
    sleep(1.0)
    inputElement = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/section/div[2]/div[2]/form/div/input")
    inputElement.send_keys(course)
    inputElement.send_keys(Keys.ENTER)
    sleep(0.5)
    inputElement = driver.find_element_by_partial_link_text(course)
    inputElement.send_keys(Keys.ENTER)
    sleep(1.0)
    inputElement = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/section/div/div[2]/form/div[2]/div[2]/input')
    inputElement.send_keys(Keys.ENTER)
    sleep(1.0)
    inputElement = driver.find_element_by_partial_link_text('Dashboard')
    inputElement.send_keys(Keys.ENTER)
    sleep(2.0)

courses=course_lists.splitlines()
for course  in courses:
    hi(course+ ' Sem 2 2021-22')
    print(course)
print("done enroling")
    
