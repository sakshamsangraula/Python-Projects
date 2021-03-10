from selenium import webdriver

chrome_web_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_web_driver_path)

# Enter the first name, last name, and email in the form and then click on the sign up button
driver.get(url="http://secure-retreat-92358.herokuapp.com/")
first_name_box = driver.find_element_by_name(name="fName")
last_name_box = driver.find_element_by_name(name="lName")
email_box = driver.find_element_by_name(name="email")

first_name = first_name_box.send_keys(input("What is your first name?: "))
last_name = last_name_box.send_keys(input("What is your last name?: "))
email = email_box.send_keys(input("What is your email address?: "))

# click on the sign up button
button = driver.find_element_by_css_selector("form button")
button.click()