# create a InternetSpeedTwitterBot class to send a tweet to a ISP when the minimum
# speed guarantees are not met
from selenium import webdriver
import time
import os

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "http://twitter.com/"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
DOWNLOAD_SPEED_PROMISED = 150
UPLOAD_SPEED_PROMISED = 10
chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")


class InternetSpeedTwitterBot:

    def __init__(self):
        # prefix variables with self so that they can be used later on
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        # go to the speed test website
        self.driver.get(url=SPEED_TEST_URL)
        time.sleep(2)
        # find and click on the go button
        go_button_class = self.driver.find_element_by_css_selector('.start-button a')
        go_button_class.click()
        # wait for 80 seconds and get download and upload speed
        time.sleep(80)
        result_container = self.driver.find_element_by_class_name("result-container-data")
        all_result_items = result_container.find_elements_by_class_name("result-item-container")
        # download speed is in the second div of all the 3 divs in all_result_items
        self.download_speed = all_result_items[1].find_element_by_css_selector(".result-data span").text
        # upload speed is in the third div of all the 3 divs in all_result_items
        self.upload_speed = all_result_items[2].find_element_by_css_selector(".result-data span").text
        print(f"download is {self.download_speed} and upload is {self.upload_speed}")
        if self.download_speed < DOWNLOAD_SPEED_PROMISED or self.upload_speed < UPLOAD_SPEED_PROMISED:
            self.tweet_at_provider()


    def tweet_at_provider(self):
        time.sleep(3)
        # go to the twitter url
        self.driver.get(url=TWITTER_URL)
        time.sleep(3)
        # get the sign up and login block
        authentication_block = self.driver.find_element_by_class_name("css-1dbjc4n")
        authentication_block_links = authentication_block.find_elements_by_css_selector("a")
        time.sleep(3)

        # click on the login button (second link)
        login_button = authentication_block_links[1]
        login_button.click()

        # enter email and password  and login
        time.sleep(3)
        form = self.driver.find_element_by_css_selector("form")
        container = form.find_element_by_class_name("css-1dbjc4n")
        email_block = container.find_element_by_name("session[username_or_email]")
        email_block.send_keys(EMAIL)
        time.sleep(3)
        password_block = container.find_element_by_name("session[password]")
        password_block.send_keys(PASSWORD)
        time.sleep(5)
        login_button = container.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login_button.click()

        # tweet :)
        time.sleep(1)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        time.sleep(2)
        # write the message
        message_section = self.driver.find_element_by_css_selector('.DraftEditor-editorContainer div div')
        message = f"Hey Internet Provider, why is my internet speed" \
                  f" {self.download_speed} down / {self.upload_speed} up when I pay " \
                  f"for 150 down / 10 up "
        message_section.send_keys(message)

        # wait for 5 seconds and click on the tweet button and send the tweet
        time.sleep(5)
        final_tweet_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]')
        final_tweet_button.click()
        print("finished tweeting:)")
        time.sleep(5)
        # close the browser completely
        self.driver.quit()

