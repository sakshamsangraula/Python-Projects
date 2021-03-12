from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=2385531169&f_L=Texas%2C%20United%20States&f_LF=f_AL&geoId=102748797&keywords=python%20developer&location=Texas%2C%20United%20States&sortBy=R"
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_L=Texas%2C%20United%20States&f_LF=f_AL&geoId=102748797&keywords=marketing&location=Texas%2C%20United%20States&sortBy=R"
chrome_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# go to the URL and sign in
time.sleep(1)
driver.get(url=LINKEDIN_URL)
pre_sign_in_button = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")
pre_sign_in_button.click()


# enter in username and password
time.sleep(1)
username_input = driver.find_element_by_id("username")
username_input.send_keys(USERNAME)
password_input = driver.find_element_by_id("password")
password_input.send_keys(PASSWORD)
main_sign_in_button = driver.find_element_by_css_selector(".login__form_action_container button")
main_sign_in_button.click()

# get all the list of jobs
time.sleep(5)
list_of_jobs = driver.find_elements_by_css_selector(".jobs-search-results__list li")
print(f"length of jobs {len(list_of_jobs)}")
for job in list_of_jobs:

    try:
        time.sleep(1)
        # click on the job and use the easy apply feature
        print(f"going to a new job called {job.text}")
        job_link = job.find_element_by_css_selector("a")
        job_link.click()
        # find a job and apply where you only have to type in your email
        time.sleep(3)

        # click on the easy apply button
        easy_apply_button = driver.find_element_by_class_name("jobs-apply-button--top-card")
        easy_apply_button.click()
        time.sleep(1)
        #enter phone number by first clearing all the text
        # YOU HAVE TO SELECT THE INPUT ATTRIBUTE TO GET RID OF THE TEXT WITH CLEAR AND THEN YOU CAN USE THE SEND KEYS
        # FUNCTION TO TYPE YOUR NUMBER
        phone_number_input = driver.find_element_by_css_selector(".fb-single-line-text input")
        phone_number_input.clear()
        time.sleep(1)
        phone_number_input.send_keys("111")

        # submit application if the button says submit
        submit_application_btn = driver.find_element_by_css_selector("footer button")
        btn_text = submit_application_btn.find_element_by_css_selector("span").text
        if btn_text == "Submit application":
            submit_application_btn.click()
            # sleep for 5 seconds for everything to load
            time.sleep(1)
            # click on the x button to exit
            x_button_class = driver.find_element_by_class_name("post-apply-modal")
            x_button = x_button_class.find_element_by_css_selector("button")
            x_button.click()
            time.sleep(2)
        else:
            # click on the x button to exit
            x_button_id = driver.find_element_by_css_selector("div button")
            # x_button_svg = x_button_id.find_element_by_css_selector("li-icon svg")
            x_button_id.click()
            time.sleep(1)
            # click on the discard button

            discard_button_class = driver.find_element_by_class_name("artdeco-modal--layer-confirmation")
            discard_button_action_bar = discard_button_class.find_element_by_class_name("artdeco-modal__actionbar")
            # pick the 2nd button
            discard_buttons = discard_button_action_bar.find_elements_by_css_selector("button")
            discard_button = discard_buttons[1]
            time.sleep(2)
            # discard_button = driver.find_element_by_css_selector(".artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
            # discard_button = driver.find_element_by_css_selector("button")
            discard_button.click()
            time.sleep(3)


    except:
        print("This is a complicated application. No thanks lol")



