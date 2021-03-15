from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
# import lxml


ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
GOOGLE_SHEETS_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScsDBJ0ihCzn55ffuhNOrw_Msm8aeBWkxCg0QKHz7O_9uR5fQ/viewform?usp=sf_link'

# Provide a user agent and language in the header so that it looks like a real browser
# is accessing the website
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    "Accept-Language": 'en-US,en;q=0.9'
}
# get the html of the webpage
response = requests.get(url=ZILLOW_URL, headers=headers)
zillow_html = response.text

#
soup = BeautifulSoup(zillow_html, "html.parser")

#
search_results_container = soup.find(id='search-page-list-container')
search_results_container_ul = search_results_container.find(name='ul')
all_lis = search_results_container_ul.find_all(name='li')

# SELECT THE ID AND THE CLASS
address_list = soup.select('#search-page-list-container .list-card-addr')
proper_address_list= []
for address in address_list:
    if "|" in address.getText():
        proper_address = str(address.getText()).split('|')[1]
    else:
        proper_address = str(address.getText())
    proper_address_list.append(proper_address)

print(proper_address_list)

price_list = soup.select('#grid-search-results .list-card-price')
proper_price_list = []

for price in price_list:
    price = price.getText()
    # if there are any strange characters in the price remove them and if the strange character is still stuck (because it does not have between it and the number)
    # then remove it using the replace function
    if "/" in price:
        proper_price = price.split('/')[0].replace("/", '')
    elif '+' in price:
        proper_price = price.split('+')[0].replace('+', '')
    elif ' ' in price:
        proper_price = price.split(' ')[0].replace('+', '')
    else:
        proper_price = price
    proper_price_list.append(proper_price)
print(proper_price_list)

all_links = soup.select("#search-page-list-container .list-card-link")
proper_links = []
for link in all_links:
    link = link.get('href')
    # if the link does not prefix with 'zillow' then add it to the link
    if "zillow" not in link:
        proper_link = f"https://www.zillow.com/{str(link)}"
    else:
        proper_link = link
    proper_links.append(proper_link)
print(proper_links)

################################# Automate filling out data to Google Sheets #####################################
chrome_driver_path = "C:\Development_Tools\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# loop through all the results from Zillow and fill out the form one at a time for all the results
for index in range(0, len(proper_address_list)):
    # go to the google sheets url
    driver.get(url=GOOGLE_SHEETS_URL)
    time.sleep(1)
    # get all the blocks with questions
    question_blocks = driver.find_elements_by_class_name(name='freebirdFormviewerViewNumberedItemContainer')
    address_input = question_blocks[0].find_element_by_css_selector("input")
    address_input.send_keys(proper_address_list[index])
    time.sleep(2)
    price_input = question_blocks[1].find_element_by_css_selector("input")
    price_input.send_keys(proper_price_list[index])
    time.sleep(2)
    link_input = question_blocks[2].find_element_by_css_selector("input")
    link_input.send_keys(proper_links[index])
    time.sleep(1)
    # click on the submit button
    submit_button = driver.find_element_by_css_selector('.freebirdFormviewerViewNavigationLeftButtons div')
    submit_button.click()
    time.sleep(5)



