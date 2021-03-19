from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
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
        search_input.send_keys(ACCOUNT_TO_FOLLOW)
        time.sleep(5)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)
        # click on the first search result
        dropdown = self.driver.find_element_by_class_name('fuqBx')
        dropdowns = dropdown.find_elements_by_css_selector('div')
        first_drop_down = dropdowns[0]
        # click on the first dropdown
        first_drop_down.click()



        # keep scrolling
        # while True:
        #     self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        #     time.sleep(5)


        # # get the current scroll height
        # previous_height = self.driver.execute_script("return document.body.ScrollHeight")
        #
        # while True:
        #     # scroll down to the bottom
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(3)
        #
        #     # calculate the new height with the previous height and if they are not equal
        #     # then make the new height the previous height
        #     new_height = self.driver.execute_script("return document.body.ScrollHeight")
        #     if new_height == previous_height:
        #         break
        #     else:
        #         previous_height = new_height


    def scroll_and_follow(self):

        # click on the follower count
        time.sleep(3)
        followers_bar = self.driver.find_element_by_class_name('k9GMp')
        all_lis = followers_bar.find_elements_by_css_selector('li')
        followers = all_lis[1]
        follower_count = str(followers.find_element_by_css_selector('span').get_attribute("title"))
        follower_count = int(follower_count.replace(",", ""))
        print(f'Follower count is {follower_count}')
        followers.click()
        time.sleep(2)
        fBody = self.driver.find_element_by_xpath("//div[@class='isgrP']")

        time.sleep(5)

        i = 0
        index = 0
        while i < follower_count:
            try:
                all_followers_lis = self.driver.find_elements_by_css_selector('.PZuss li')

                for _ in range(0, len(all_followers_lis)):
                    time.sleep(5)
                    follow_button = all_followers_lis[index].find_element_by_css_selector('button')
                    print(follow_button.text)
                    follow_button.click()
                    time.sleep(3)
                    i += 1
                    index += 1
            except NoSuchElementException:
                self.driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight + arguments[0].offsetHeight;", fBody
                )
                time.sleep(1)
                all_followers_lis = self.driver.find_elements_by_css_selector('.PZuss li')

            except IndexError:
                self.driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight + arguments[0].offsetHeight;", fBody
                )
                time.sleep(1)
                all_followers_lis = self.driver.find_elements_by_css_selector('.PZuss li')

            except ElementClickInterceptedException:
                #cancel the popup asking us to unfollow the people
                # we already follow if we try to follow them again
                buttons = self.driver.find_elements_by_css_selector('.piCib button')
                cancel_button = buttons[1]
                cancel_button.click()
                index += 1
                time.sleep(2)



        # time.sleep(5)
        # # follow all accounts one at a time
        # for li in all_followers_lis:
        #     follow_button = li.find_element_by_css_selector('.isgrP .Pkbci')
        #     follow_button.click()
        #     time.sleep(2)
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", fBody)



insta_follower_bot = InstaFollower()
insta_follower_bot.login()
insta_follower_bot.find_followers()
insta_follower_bot.scroll_and_follow()