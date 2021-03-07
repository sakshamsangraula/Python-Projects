from bs4 import BeautifulSoup
import requests
import pandas

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://www.afi.com/afis-100-years-100-movies/"

# get and parse the html from the website
response = requests.get(URL)
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")

# create a dictionary with the key of the number and value of the title and year
all_h6s = soup.find_all(name="h6", class_="q_title")
complete_info = {h6.getText().split(".")[0]: f"{h6.getText().split('.')[1]}" for h6 in all_h6s}

# output the data to a new file
with open("top_100_movies.txt", mode="w") as top100file:
    # iterate over the dictionary with .items() method
   top100file.write("Starting to write\n")
   print(complete_info)
   for (key, val) in complete_info.items():
       top100file.write(f"{key} {val}\n")
   top100file.write("finished writing")


