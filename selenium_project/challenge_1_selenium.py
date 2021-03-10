from selenium import webdriver
chrome_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(url="https://www.python.org")


# create a dictionary with the date and event
event_info = {}

# find the event widget and then menu class
calendar = driver.find_element_by_class_name(name="event-widget")
# USE ELEMENTS with an S so that we get a list
calendar_time_list = calendar.find_elements_by_css_selector("li time")
calendar_event_names = calendar.find_elements_by_css_selector("li a")

for index in range(0, len(calendar_time_list)):
    event_info[index] = {
        "time": calendar_time_list[index].text,
        "name": calendar_event_names[index].text,
        "link": calendar_event_names[index].get_attribute("href")
    }
print(event_info)



