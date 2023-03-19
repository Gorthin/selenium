import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchProductTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("https://magento2-demo.magebit.com/")

    def test_search_by_category(self):

        # get the search textbox
        self.search_field = self.driver.find_element(By.ID, "search")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("phone")
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver\
            .find_elements(By.XPATH, "//div[@class='products wrapper grid products-grid']/ol[@class='products list items product-items']/li")

        # check count of products shown in results
        self.assertEqual(4, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
