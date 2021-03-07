from bs4 import BeautifulSoup
import lxml

#
# # read the contents of the html file (also specify the encoding to utf8 to be safe)
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# # provide the content in string format and the parser
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
#
# print(soup.p)

with open("website.html", encoding="utf8") as file:
    contents = file.read()

# initialize the soup object with the contents and the parser
soup_obj = BeautifulSoup(contents, "html.parser")

# find all paragraphs
# all_ps = soup_obj.find_all(name="p")
# print(all_ps)

# find all links
# all_links = soup_obj.find_all(name="a")
# print(all_links)

# get text of all the links, and href of all links
# all_links = soup_obj.find_all(name="a")
# for link in all_links:
#     text = link.getText()
#     href = link.get("href")
#     print(f"Text is {text} and href is {href}")

# get first item that is h1 and has id of name
# first_h1_with_id_name = soup_obj.find(name="h1", id="name")
# print(first_h1_with_id_name)

# get first item that is h3 and has class of heading
# first_h3_with_class = soup_obj.find(name="h3", class_="heading")
# print(first_h3_with_class)

# - get text
# - get name
# - get class value
# text = first_h3_with_class.get_text()
# name = first_h3_with_class.name
# class_val = first_h3_with_class.get("class")
# print(f"Text is {text} name is {name} class val is {class_val}")

# use css selector to get the first a in p
# first_a_in_p = soup_obj.select("p a")
# print(first_a_in_p)

# use css selector to get the first id (name)
first_id_name = soup_obj.select_one("#name")
print(first_id_name)

# select all elements that have a class of heading
all_elems_with_class = soup_obj.select(".heading")
print(all_elems_with_class)