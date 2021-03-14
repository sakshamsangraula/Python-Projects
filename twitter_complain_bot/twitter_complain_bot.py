# create a InternetSpeedTwitterBot class to send a tweet to a ISP when the minimum
# speed guarantees are not met
from selenium import webdriver
import time

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "http://twitter.com/"

chrome_driver_path = "C:\Development_Tools\chromedriver.exe"

class InternetSpeedTwitterBot:

    def __init__(self):
        # prefix variables with self so that they can be used later on
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        # go to the speed test website
        self.driver.get(url=SPEED_TEST_URL)
        time.sleep(5)
        # find and click on the go button
        go_button_class = self.driver.find_element_by_css_selector('.start-button a')
        go_button_class.click()
        # wait for 2 minutes and get download and upload speed
        time.sleep(180)
        result_container = self.driver.find_element_by_class_name("result-container-data")
        all_result_items = result_container.find_elements_by_class_name("result-item-container")
        # download speed is in the second div of all the 3 divs in all_result_items
        self.download_speed = all_result_items[1].find_element_by_css_selector(".result-data span").text
        # upload speed is in the third div of all the 3 divs in all_result_items
        self.upload_speed = all_result_items[2].find_element_by_css_selector(".result-data span").text
        print(f"down is {self.download_speed} and upload is {self.upload_speed}")

    def tweet_at_provider(self):
        # login to twitter
        self.driver.get(url=TWITTER_URL)
        time.sleep(5)
        # get the sign up and login block
        authentication_block = self.driver.find_element_by_class_name("css-1dbjc4n")
        authentication_block_links = authentication_block.find_elements_by_css_selector("a")
        time.sleep(5)
        # click on the login button (second link)
        login_button = authentication_block_links[1]
        login_button.click()
        # enter email and password  and login
        time.sleep(10)
        email_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]')
        email_input.send_keys("test@gmail.com")
