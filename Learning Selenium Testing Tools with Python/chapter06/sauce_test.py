import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchProducts(unittest.TestCase):

    PLATFORM = 'WINDOWS'
    BROWSER = 'firefox'
    SAUCE_USERNAME = 'upgundecha'
    SUACE_KEY = 'c6e7132c-ae27-4217-b6fa-3cf7df0a7281'

    def setUp(self):

        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browserName'] = self.BROWSER

        sauce_string = self.SAUCE_USERNAME + ':' + self.SUACE_KEY

        self.driver = \
            webdriver.Remote('http://' + sauce_string + '@ondemand.saucelabs.com:80/wd/hub', desired_caps)
        self.driver.get('https://magento2-demo.magebit.com/')
        self.driver.implicitly_wait(30)
		self.driver.maximize_window()

    def testSearchByCategory(self):

        # get the search textbox
        self.search_field = self.driver.find_element(By.NAME, 'q')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.\
            find_elements(By.XPATH, "//div[@class='products wrapper grid products-grid']/ol[@class='products list items product-items']/li")

        # check count of products shown in results
        self.assertEqual(2, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SearchProducts.BROWSER = sys.argv.pop()
        SearchProducts.PLATFORM = sys.argv.pop()
    unittest.main(verbosity=2)
