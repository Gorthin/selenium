import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("https://magento2-demo.magebit.com/")
        cls.driver.title

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element(By.NAME, "q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.\
            find_elements(By.XPATH, "//ol[@class='products list items product-items']/li")
        self.assertEqual(4, len(products))
        time.sleep(2)

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element(By.NAME, "q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("salt shape")
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.\
            find_elements(By.XPATH, "//ol[@class='products list items product-items']/li")
        self.assertEqual(8, len(products))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()