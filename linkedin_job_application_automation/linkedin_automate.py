from selenium import webdriver
import time
import os
from selenium.common.exceptions import NoSuchElementException


LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102748797&keywords=python%20developer&location=Texas%2C%20United%20States&sortBy=R"
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=2437341514&f_L=Texas%2C%20United%20States&f_LF=f_AL&geoId=102748797&keywords=python%20developer&location=Texas%2C%20United%20States&sortBy=R"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
# create a driver that works with the Google Chrome driver
chrome_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# login to the linkedin URL
driver.get(url=LINKEDIN_URL)

# sleep for 2 seconds to let the page load fully
time.sleep(2)

# sign in to linkedin
sign_in_button = driver.find_element_by_xpath('/html/body/header/nav/div/a[2]')
sign_in_button.click()

# type in the username and password and sign in
username_input = driver.find_element_by_id(id_="username")
username_input.send_keys(USERNAME)
password_input = driver.find_element_by_id(id_="password")
password_input.send_keys(PASSWORD)
real_sign_in_button = driver.find_element_by_css_selector(".login__form_action_container button")
real_sign_in_button.click()

# give about 2 seconds for the page to load
time.sleep(5)
# apply for a job

# get a list of jobs

all_listings = driver.find_elements_by_class_name("jobs-search-results__list-item")
try:
    for job in all_listings:
        print(job.text)
        print("\n\n")
        time.sleep(2)
    # sleep for 2 seconds
    # click on the easy apply button
    easy_apply = driver.find_element_by_class_name(name="jobs-apply-button--top-card")
    easy_apply.click()
    # wait for 5 seconds before sending the keys
    time.sleep(5)

except NoSuchElementException:
    print("Exception happened")
# fill out the phone number and submit (email and country code is already filled in)

# INCLUDE THE CLASS NAME AND WHAT WE WANT TO INTERACT WITH (HERE IT'S INPUT)
phone_input = driver.find_element_by_class_name("fb-single-line-text__input")
if phone_input.text == "":
    phone_input.click()
    phone_input.send_keys("111-222-3333")

# wait 5 seconds
time.sleep(5)
# click the submit button and submit the application
submit_app = driver.find_element_by_css_selector("footer button")
print(submit_app.text)
submit_app.click()

