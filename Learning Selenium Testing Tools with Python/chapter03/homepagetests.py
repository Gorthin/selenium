import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('https://magento2-demo.magebit.com/')

    def test_search_text_field_max_length(self):
        # get the search textbox
        search_field = self.driver.find_element(By.ID, "search")

        # check maxlength attribute is set to 128
        self.assertEqual("128", search_field.get_attribute("maxlength"))

    def test_search_button_enabled(self):
        # get Search button
        search_button = self.driver.find_element(By.CLASS_NAME, "button")

        # check Search button is enabled
        self.assertTrue(search_button.is_enabled())

    def test_my_account_link_is_displayed(self):
        # get the Account link
        account_link = self.driver.find_element(By.LINK_TEXT, "Create an Account")

        # check My Account link is displayed/visible in the Home page footer
        self.assertTrue(account_link.is_displayed())

    def test_account_links(self):
        # get the all the links with Account text in it
        account_links = self.driver.\
            find_elements(By.PARTIAL_LINK_TEXT, "Account")

        # check Account and My Account link is displayed/visible in the Home page footer
        self.assertTrue(len(account_links), 2)

    def test_count_of_promo_banners_images(self):
        # get promo banner list
        banner_list = self.driver.find_element(By.CLASS_NAME, "block-promo home-pants")

        # get images from the banner_list
        banners = banner_list.find_elements(By.TAG_NAME, "img")

        # check there are 3 banners displayed on the page
        self.assertEqual(1, len(banners))

    def test_shopping_cart_status(self):
        # check content of My Shopping Cart block on Home page
        # get the Shopping cart icon and click to open the Shopping Cart section
        shopping_cart_icon = self.driver.\
            find_element(By.CSS_SELECTOR, "a.action.showcart:nth-child(1)")
        shopping_cart_icon.click()

        # get the shopping cart status
        shopping_cart_status = self.driver.\
            find_element(By.CSS_SELECTOR, "strong.subtitle.empty").text
        self.assertEqual("You have no items in your shopping cart.", 
                          shopping_cart_status)
        # close the shopping cart section
        close_button = self.driver.\
            find_element(By.CSS_SELECTOR, "#btn-minicart-close")
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
