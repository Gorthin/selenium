import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchProducts(unittest.TestCase):

    PLATFORM = 'WINDOWS	'
    BROWSER = 'firefox'

    def setUp(self):

        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browserName'] = self.BROWSER

        self.driver = \
            webdriver.Remote('http://192.168.1.104:4444/wd/hub', desired_caps)
        self.driver.get('https://magento2-demo.magebit.com/')
        self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		

    def test_search_by_category(self):

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
