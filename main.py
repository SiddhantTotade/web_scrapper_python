# S1 - Get the html
# S2 - Parse the html
# S3 - Html tree traversal

import requests
from bs4 import BeautifulSoup

url = "https://www.airtel.in/myplan-infinity/"

# Getting the html
r = requests.get(url)
htmlContent = r.content

# Parsing the html
soup = BeautifulSoup(htmlContent, 'html.parser')

# Html tree traversal
# title = soup.title

# print(type(soup))
# print(type(title))
# print(type(title.string))

# paras = soup.find('p')
# anchor = soup.find_all('a')
# find_all_element_of_same_class = soup.find("div",class_="root")

# print(soup.find('a').get_text())

# anchor = soup.find_all('a')
# all_links = set()

# for link in anchor:
#     if(link.get('href') != '#'):
#         linkText = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi/"+link.get('href')
#         all_links.add(link)
#         print(linkText)


# ids = soup.find(id='panels')
# for elem in ids.children:
#     print(elem)

# for item in ids.stripped_strings:
#     print(item)

# for item in ids.stripped_strings:
#     print(item)

# for item in ids.parents:
#     print(item.name)

# print(ids.previous_sibling.previous_sibling)

# elem = soup.select('#panels')
# print(elem)

elem = soup.find('div',class_='previous_homepage')
print(elem)
