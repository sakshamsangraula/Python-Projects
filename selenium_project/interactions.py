from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# get the number from the wikipedia article
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
total_articles_in_english_id = driver.find_element_by_id(id_="articlecount")
total_articles_in_english_a = total_articles_in_english_id.find_element_by_css_selector("a")
total_articles_in_english = total_articles_in_english_a.text

# click on the total article number
# total_articles_in_english_a.click()

# use the in-built functionality to click on a link text
# all_portals_text = driver.find_element_by_link_text(link_text="All portals")
# all_portals_text.click()

# search and enter the word "python" in the search bar in wikipedia
search_bar = driver.find_element_by_name(name="search")
search_bar.send_keys("Python")
# hit the enter key by importing a library with constants
search_bar.send_keys(Keys.ENTER)



# close the entire browser at the end
# driver.quit()