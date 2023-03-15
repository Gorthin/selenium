import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new Chrome session
driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("https://magento2-demo.magebit.com/")

# get the search textbox
search_field = driver.find_element(By.NAME, "q")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("phones")
search_field.click()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements(By.XPATH, "//h2[@class='product-name']/a")

# get the number of anchor elements found
print("Found " + str(len(products)) + " products:")

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print(product.text)

# close the browser window
driver.quit()
