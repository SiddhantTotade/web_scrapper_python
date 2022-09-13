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

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("https://www.airtel.in/myplan-infinity/")

elem = driver.find_elements(By.CLASS_NAME, "price")

for item in elem:
    print(item.text)
