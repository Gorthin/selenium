import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By


@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("https://magento2-demo.magebit.com/")

    # specify test data using @data decorator
    @data(("phones", 4), ("music", 2))
    @unpack
    def test_search(self, search_value, expected_count):
        # get the search textbox
        self.search_field = self.driver.find_element(By.NAME, "q")
        self.search_field.clear()

        # enter search keyword and submit.
        # use search_value argument to pass data
        self.search_field.send_keys(search_value)
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver\
            .find_elements(By.XPATH, "//div[@class='products wrapper grid products-grid']/ol[@class='products list items product-items']/li")

        # check count of products shown in results
        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
