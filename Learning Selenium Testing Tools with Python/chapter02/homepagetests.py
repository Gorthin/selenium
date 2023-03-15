import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from __builtin__ import classmethod


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Firefox session """
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page """
        cls.driver.get("https://magento2-demo.magebit.com/")

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_create_account(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.ID, "idaaMzaSPz"))

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = self.driver.\
            find_element(By.CSS_SELECTOR, "a.action.showcart:nth-child(1)")
        shopping_cart_icon.click()

        shopping_cart_status = self.driver.\
            find_element(By.CSS_SELECTOR, "strong.subtitle.empty").text
        self.assertEqual("You have no items in your shopping cart.",
                          shopping_cart_status)

        close_button = self.driver.\
            find_element(By.CSS_SELECTOR, "#btn-minicart-close")
        close_button.click()

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)
