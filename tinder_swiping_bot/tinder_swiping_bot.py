from selenium import webdriver
import time
import os

# CONSTANTS
TINDER_URL = "https://tinder.com/"
EMAIL = os.environ.get("email")
PASSWORD = os.environ.get("password")

chrome_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# go to tinder and login with facebook
driver.get(url=TINDER_URL)
log_in_button = driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
time.sleep(5)
log_in_button.click()
time.sleep(5)
login_with_facebook_button = driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_with_facebook_button.click()
time.sleep(10)

# tell selenium to go to the facebook window in chrome since facebook opens up in a new tab
tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)
print(driver.title)

time.sleep(5)
email_input = driver.find_element_by_id("email")
email_input.send_keys(EMAIL)
time.sleep(5)
password_input = driver.find_element_by_id("pass")
password_input.send_keys(PASSWORD)
time.sleep(5)
facebok_login_button = driver.find_element_by_name(name="login")
facebok_login_button.click()
time.sleep(5)

# switch back to the tinder window
driver.switch_to.window(tinder_window)
print(driver.title)


