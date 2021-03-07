from bs4 import BeautifulSoup
import requests

# get and parse html from the website
response = requests.get("https://news.ycombinator.com/")
website_html = response.text

soup_obj = BeautifulSoup(website_html, "html.parser")

# get information for all the links
link_total = soup_obj.find(name="a", class_="storylink")
link_title = link_total.getText()
link = link_total.get("href")
link_upvote = soup_obj.find(name="span", class_="score").getText()
print(f"link title is {link_title} link is {link} upvote is {link_upvote}")


articles = soup_obj.find_all(name="a", class_="storylink")
article_titles = [article.getText() for article in articles]
print(article_titles)
article_links = [ article.get("href") for article in articles]
print(article_links)
article_upvotes = [int(span.getText().split()[0]) for span in soup_obj.find_all(name="span", class_="score")]
print(article_upvotes)

# # get the highest score and the corresponding title and link
# highest_score = 0
# for score in article_upvotes:
#     if score > highest_score:
#         highest_score = score
#         index = article_upvotes.index(highest_score)

highest_score = max(article_upvotes)
index = article_upvotes.index(highest_score)
print(f"The highest score is {highest_score}\n"
      f"title is {article_titles[index]}\n"
      f"link is {article_links[index]}")


