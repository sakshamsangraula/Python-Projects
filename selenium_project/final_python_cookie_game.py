from selenium import webdriver
import time
import random
import math

URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_webdriver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_webdriver_path)

driver.get(url=URL)
cookie = driver.find_element_by_id("cookie")

timeout = 5
time_start = time.time()
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
CLICK_TRACKER = 1

while True:
    time.sleep(0.1)
    cookie.click()


    # if it has been more than 5 seconds then find out which upgrade we can get and get
    # the most expensive upgrade
    if time.time() > time_start + timeout:

        # get the list of upgrades in the right side
        all_upgrades = driver.find_elements_by_css_selector("#store b")
        upgrade_prices = []
        for upgrade in all_upgrades:
            upgrade_text = upgrade.text
            # if an upgrade's price is available then add it to the list
            if upgrade_text != "":
                price = int(str((upgrade_text)).split(" - ")[1].replace(",", ""))
                upgrade_prices.append(price)

        # create a dictionary with key as item name and value as price
        upgrade_info = {}
        # have to do -1 because the last upgrade doesn't exist
        for index in range(0, len(item_ids)-1):
            upgrade_info[index] = {
                item_ids[index]: upgrade_prices[index]
            }


         # get the current money
        current_money = int(str(driver.find_element_by_id("money").text).replace(",", ""))

        affordable_upgrades = [price for price in upgrade_prices if current_money > price]
        if len(affordable_upgrades) >= 1:
            max_price = max(affordable_upgrades)

        # if click tracker is odd then run the code if it's even then skip
        # this gives us more chance to get the cookie to be a higher number
        # so that we also get a chance to buy other upgrades (not just cursor)
        randNum = random.randint(1, 5)
        if randNum == 5 or math.fabs(current_money - max_price) > 50 :

            # if the current money is greater than max by less than 20 points then click on the max
            if current_money > max_price:
                index = upgrade_prices.index(max_price)
                upgrade_id = item_ids[index]
                driver.find_element_by_id(upgrade_id).click()

        print(upgrade_info)



