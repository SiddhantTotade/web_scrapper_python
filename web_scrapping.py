# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get("https://chromedriver.chromium.org/getting-started")
# driver.implicitly_wait(10)

# class_list = driver.find_elements(
#     By.XPATH, "//div[contains(@class,'single_cart')]")

# for list in class_list:
#     print(list.text)

# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# brave_path = "/etc/alternatives/brave-browser"
# options = webdriver.ChromeOptions()
# options.binary_location = brave_path
# driver = webdriver.Chrome("/usr/lib64/chromium-browser/chromedriver")
# driver.maximize_window()

# driver.get(url="https://www.airtel.in/myplan-infinity/")

# driver.find_element()


# class_list = driver.find_element(
#     By.XPATH, "//span[contains(@class,'price')]")

# print(type(class_list))

# driver.quit()

# -----------------------------------
# from lib2to3.pgen2 import driver
# from selenium import webdriver

# driver_location = "/home/siddhanttotade/Downloads/chromedriver_linux64/chromedriver"
# binary_location = "home/siddhanttotade/usr/lib64/chromium-browser/chromium-browser.sh"

# option = webdriver.ChromeOptions()
# option.binary_location = binary_location

# driver = webdriver.Chrome(
#     executable_path=driver_location, chrome_options=option)

# driver.get("https://www.youtube.com")

# print(driver.page_source.encode('utf-8'))

# driver.quit()

# ---------------------------------------

from math import floor
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("https://www.airtel.in/myplan-infinity/")

# elem = driver.find_elements(By.CLASS_NAME, "border-bottom")

# elem = driver.find_elements(
#     By.XPATH, "//span[contains(@class,'border-bottom')]")

# elem = driver.find_elements(
#     By.XPATH, "//div[@class,'border-bottom']/span")

elem = driver.find_elements(
    By.CSS_SELECTOR, "div.border-bottom > span:first-child")

data_list = []

# print(len(elem))

# for i in len(elem):
#     data_list.append([])
#     for j in elem:
#         if (j.text == "N/A" or j.text == "YES"):
#             data_list[i].append(j.text)
#             break
#         data_list[i].append(j.text)

for i in elem:
    data_list.append(i.text)

# print(type(len(data_list)))
# print(data_list)

# print(floor(len(data_list)/5))
storelist = []

for i in range(floor(len(data_list)/4)):
    for j in range(floor(len(data_list)/4)):
        temp_list = [i][j]
        # if(data_list[j] == 'N/A' or data_list[j] == 'YES'):
        #     temp_list.append(data_list[j])
        #     break
        temp_list.append(data_list[j])
    storelist.append(temp_list)

print(storelist)
