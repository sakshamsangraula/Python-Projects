from selenium import webdriver
import time
import datetime as dt
import threading

chrome_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id(id_="cookie")
highest = 0

def check_store():
    store = driver.find_element_by_id(id_="store")
    stores = store.find_elements_by_css_selector("div")
    # find gray stores
    gray_stores = store.find_elements_by_class_name("grayed")
    white_stores = [store for store in stores if store not in gray_stores]

    # click on white store
    global highest
    try:
        # get all the points
        store_points = []
        for store in white_stores:
            store_point = store.find_element_by_css_selector("b")
            store_point = int(store_point.text.split(" - ")[1])
            store_points.append(store_point)

        print(store_points)

        # find the highest white store and click on it
        for index in range(0, len(store_points)):
            print(f"Current points is{current_point} and highest is {highest}")
            current_point = store_points[index]
            if current_point > highest:
                highest = current_point
                click_on = index
                print("found highest")
        print("clicking")
        white_stores[click_on].click()
        print("clicked")

    except:
        print("Can't click yet, it turned gray again")

# keep clicking on cookies
while True:
    time_start = dt.datetime.now()
    time_start_seconds = str(time_start).split()[1].split(":")[2].split(".")[0]

    # if it's 5 seconds check the right hand side and see if we can buy anything
    if int(time_start_seconds) % 5 == 0:
        #call the check store function
        check_store()
#
# def check_store():
#     white_stores = []
#     # get the entire store
#     stores = driver.find_elements_by_id(id_="store")
#     # find a white background store and then click on it
#
#     # find all stores that are gray
#     gray_stores = driver.find_elements_by_class_name(name="grayed")
#     for store in stores:
#         if store not in gray_stores:
#             # white_stores.append(store)
#             store.click()
#
#     # click on all the white stores
#     # for store in white_stores:
#     #     store.click()
#
#
#
# # continue clicking on the cookie and check every 5 seconds to see what is available to
# # purchase in the right side
# def printit():
#   threading.Timer(5.0, printit).start()
#   cookie.click()
#   check_store()
#
# printit()
#
#
