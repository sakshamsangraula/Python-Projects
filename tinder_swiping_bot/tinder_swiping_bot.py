from selenium import webdriver
import time
import os

# CONSTANTS
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

TINDER_URL = "https://tinder.com/"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(chrome_driver_path)

# go to tinder and login with facebook
driver.get(url=TINDER_URL)
time.sleep(3)
login_button = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()
time.sleep(3)
login_with_facebook_button = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_with_facebook_button.click()

# login using facebook and then switch back to tinder
# switch to facebook's window
tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)
time.sleep(2)
email_input = driver.find_element_by_id('email')
email_input.send_keys(EMAIL)
time.sleep(2)
password_input = driver.find_element_by_id('pass')
password_input.send_keys(PASSWORD)
time.sleep(2)
login_button = driver.find_element_by_name('login')
login_button.click()
time.sleep(5)

# switch back to tinder's screen
driver.switch_to.window(tinder_window)
time.sleep(2)
# after logging in allow location use, not interested in notification,
# and accept cookies
location_use_allow_button = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div/div/div[3]/button[1]')
time.sleep(2)
location_use_allow_button.click()
accept_cookies_button = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[2]/div/div/div[1]/button')
accept_cookies_button.click()
time.sleep(2)
not_interested_notifications_button = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div/div/div[3]/button[2]')
not_interested_notifications_button.click()
time.sleep(2)

# dislike people 100 times since the free version only allows 100 swipes a day
for index in range(0, 100):
    # dislike people and handle exceptions
    try:
        dislike_button = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_button.click()
        time.sleep(2)
        print(index)
    # if there is an exception then sleep for some time
    except NoSuchElementException:
        time.sleep(2)
    # if it's a match then click on the go back to tinder button to find more people
    # won't happen in this case since the bot is disliking everyone
    except ElementClickInterceptedException:
        time.sleep(2)
        print("Clicked on the go back to tinder button")
        time.sleep(1)

        # there might also be a notification to add tinder to home screen and for
        # that case, click on the not interested button
        not_interested_button_home_screen = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[2]/button[2]')
        not_interested_button_home_screen.click()
        time.sleep(2)




