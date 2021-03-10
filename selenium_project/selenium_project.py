from selenium import webdriver

# set the path to the raw string
chrome_driver_path = r"C:\Development_Tools\chromedriver.exe"

# create a selenium driver that connects to the chrome driver so selenium can work
# with the latest version of google chrome
selenium_driver = webdriver.Chrome(executable_path=chrome_driver_path)

# get amazon's website and close it
# selenium_driver.get("https://www.amazon.com/gp/product/B07W55DDFB?pf_rd_r=MD9W23B11V5R7621ME35&pf_rd_p=5ae2c7f8-e0c6-4f35-9071-dc3240e894a8&pd_rd_r=c7572226-d81a-4d89-968a-362bbb5f69ec&pd_rd_w=H2M8u&pd_rd_wg=nXueG&ref_=pd_gw_unk")
#
# ######################## Find element by ID #######################3
# price_element = selenium_driver.find_element_by_id("priceblock_ourprice")
# price = price_element.text
# print(price)

########################## Get Tagname and placeholder attributes ##################

# selenium_driver.get(url="https://www.python.org")
# search_bar = selenium_driver.find_element_by_name("q")
# tag_name = search_bar.tag_name
# placeholder = search_bar.get_attribute("placeholder")
# print(f"Tag name is {tag_name}, and placeholder is {placeholder}")

########################### Find Element by Classname ###########################

# selenium_driver.get(url="https://www.python.org")
# logo = selenium_driver.find_element_by_class_name(name="python-logo")
# size = logo.size
# print(size)

########################### Find Element by CSS selector #########################

# selenium_driver.get(url="https://www.python.org")
# link_element = selenium_driver.find_element_by_css_selector(".documentation-widget a")
# link = link_element.get_attribute("href")
# print(link)

########################### Find Element by X Path ##############################

selenium_driver.get(url="https://www.python.org")
bug_element = selenium_driver.find_element_by_xpath(xpath='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
bug_link = bug_element.get_attribute("href")
bug_text = bug_element.text
print(f"{bug_link}: {bug_text}")












# # close --> closes a single tab
# selenium_driver.close()

# # quit --> closes the entire browser
# selenium_driver.quit()
