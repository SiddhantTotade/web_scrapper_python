# S1 - Get the html
# S2 - Parse the html
# S3 - Html tree traversal

import requests
from bs4 import BeautifulSoup

url = "https://www.airtel.in/myplan-infinity/"

# Getting the html

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Parsing the html

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Html tree traversal
title = soup.find_all('title')
print(title)
