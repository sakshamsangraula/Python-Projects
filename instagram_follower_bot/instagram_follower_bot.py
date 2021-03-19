from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

CHROME_DRIVER_PATH = "C:\Development_Tools\chromedriver.exe"
ACCOUNT_TO_FOLLOW = "cristiano"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
INSTAGRAM_LOGIN_URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:

    def __init__(self):
        # create the driver
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)


    # login to instagram with username and password
    def login(self):
        self.driver.get(url=INSTAGRAM_LOGIN_URL)
        time.sleep(5)
        username_input = self.driver.find_element_by_name(name="username")
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element_by_name(name="password")
        password_input.send_keys(PASSWORD)
        time.sleep(5)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login_button.click()

    def find_followers(self):
        time.sleep(5)
        # search for the account we want to follow
        search_input = self.driver.find_element_by_css_selector('nav input')
        time.sleep(1)
        search_input.send_keys(input("What account would you like to search for?: "))
        time.sleep(5)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)
        # click on the first search result
        dropdown = self.driver.find_element_by_class_name('fuqBx')
        dropdowns = dropdown.find_elements_by_css_selector('div')
        first_drop_down = dropdowns[0]
        # click on the first dropdown
        first_drop_down.click()

        # click on the follower count
        time.sleep(1)
        followers_bar = self.driver.find_element_by_class_name('k9GMp')
        all_lis = followers_bar.find_elements_by_css_selector('li')
        followers = all_lis[1]
        followers.click()

        # get the current scroll height
        previous_height = self.driver.execute_script("return document.body.ScrollHeight")

        while True:
            # scroll down to the bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            # calculate the new height with the previous height and if they are not equal
            # then make the new height the previous height
            new_height = self.driver.execute_script("return document.body.ScrollHeight")
            if new_height == previous_height:
                break
            else:
                previous_height = new_height


    def follow(self):

        pass


insta_follower_bot = InstaFollower()
insta_follower_bot.login()
insta_follower_bot.find_followers()
insta_follower_bot.follow()