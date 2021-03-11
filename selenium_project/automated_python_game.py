from selenium import webdriver
import time
import datetime as dt
import threading

chrome_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id(id_="cookie")
highest = 0
store_points = []



def check_store():
    store = driver.find_element_by_id(id_="store")
    stores = store.find_elements_by_css_selector("div")
    # find gray stores
    gray_stores = store.find_elements_by_class_name("grayed")
    white_stores = [store for store in stores if store not in gray_stores]

    # click on white store
    global highest

    try:
        global store_points
        # only do this for stores in white
        for store in white_stores:
            # get all the points
            all_points = store.find_elements_by_css_selector("b")

        for index in range(0, len(all_points)):
            if index < 8:
                store_point = int((str(all_points[index].text).split(" - ")[1]).replace(",", ""))
                store_points.append(store_point)
                time.sleep(10)
        print(f"Now there are {len(store_points)} num items")

        # find the highest white store and click on it
        max_point = max(store_points)
        current_money = int(driver.find_element_by_id("money").text)
        print(f"Current money is {current_money} and max is {max_point}")
        for point in store_points:
            print(f"Point is {point} and index is {store_points.index(point)}")
            time.sleep(10)


        if current_money >= max_point:
            # find max point's index and click on it
            index = store_points.index(max_point)
            white_stores[index].click()
            print(f"clicked on index {white_stores[index].text} and index is {index}")

    except:
        print("Can't click yet, it turned gray again")

# keep clicking on cookies
while True:
    time_start = dt.datetime.now()
    time_start_seconds = str(time_start).split()[1].split(":")[2].split(".")[0]
    cookie.click()
    # if it's 5 seconds check the right hand side and see if we can buy anything
    if int(time_start_seconds) % 5 == 0:
        #call the check store function
        check_store()
        time.sleep(3)
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
