from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import os
import time

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
CHROME_DRIVER_PATH = "C:\Development_Tools\chromedriver.exe"
INSTAGRAM_URL = "http://www.instagram.com"
ACCOUNT_NAME = "adidas"

class InstagramBot:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        # go to the url and login with username and password
        self.driver.get(url=INSTAGRAM_URL)
        time.sleep(2)
        username_input = self.driver.find_element_by_name(name='username')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element_by_name(name='password')
        password_input.send_keys(PASSWORD)
        time.sleep(2)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login_button.click()

    def follow(self):
        time.sleep(2)
        # click on the followers button
        followers_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]')
        follower_count = followers_button.find_element_by_css_selector('span').get_attribute('title')
        follower_count = int(follower_count.replace(",", ""))
        followers_button.click()
        time.sleep(2)

        follower_panel = self.driver.find_element_by_css_selector('.isgrP ul')
        # follow people
        #try:
        i = 0
        while i < follower_count:
         try:
            time.sleep(2)
            all_followers = self.driver.find_elements_by_css_selector('.isgrP li')
            time.sleep(2)
            for _ in range(0, len(all_followers)):
                time.sleep(1)
                follow_button = all_followers[i].find_element_by_css_selector('button')
                time.sleep(4)
                follow_button.click()
                time.sleep(4)
                i += 1

        # if Element Not Found Exception is given then scroll down by setting the top
        # to the current height
         except NoSuchElementException:
             print("scroll happened")
             time.sleep(1)
             self.driver.execute_script(
                 "arguments[0].scrollTop = arguments[0].scrollHeight", follower_panel
             )
             time.sleep(2)

         except IndexError:
             print("Index error happened")
             # if it's an index error then just sleep for some time since the bot
             # is going too fast
             time.sleep(4)

         except ElementClickInterceptedException:
             print("cancel button happened")
             cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
             cancel_button.click()
             time.sleep(2)
             # DON'T DO THIS: SKIPS PEOPLE
             # i += 1

         except StaleElementReferenceException:
                time.sleep(2)


        # except:
        #     print("exit")





    def find_followers(self):
        time.sleep(2)
        # search for the account
        search_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_button.send_keys(ACCOUNT_NAME)
        search_button.send_keys(Keys.ENTER)
        time.sleep(2)
        # find the first item in the dropdown and click on it
        dropdown_list = self.driver.find_elements_by_css_selector(".fuqBx div")
        first_dropdown = dropdown_list[0]
        first_dropdown.click()
        time.sleep(2)
        self.follow()




# initialize the bot, login and then find followers
bot = InstagramBot()
bot.login()
bot.find_followers()
