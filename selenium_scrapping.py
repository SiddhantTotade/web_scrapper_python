from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("https://www.airtel.in/myplan-infinity/")

# Getting card value
# elem = driver.find_elements(By.CLASS_NAME, "border-bottom")

# Getting card value
# elem = driver.find_elements(
#     By.XPATH, "//span[contains(@class,'border-bottom')]")

# Getting card inside value
# elem = driver.find_elements(
#     By.XPATH, "//div[@class,'border-bottom']/span")

# Getting card inside value
elem = driver.find_elements(
    By.CSS_SELECTOR, "div.border-bottom > span:first-child")

data_list = []

for i in elem:
    print(i.text)
