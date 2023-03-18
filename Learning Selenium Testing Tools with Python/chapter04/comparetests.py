from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("https://magento2-demo.magebit.com/")

    def test_compare_products_removal_alert(self):
        # get the search textbox
        search_field = self.driver.find_element(By.NAME, "q")
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys("phone")
        search_field.submit()

        # click the Add to compare link
        self.driver.\
            find_element(By.XPATH, "//div[@id='product-item-info_2']//div[@class='product details product-item-details']//div[@class='product-item-inner']//div[@class='product actions product-item-actions']//div[@class='actions-secondary']//a[@class='action tocompare']").click()
        
        # click Compare Products
        self.driver.\
            find_element(By.LINK_TEXT, "Compare Products").click()


        # click on Remove this item link,
        # this will display an alert to the user
        self.driver.find_element(By.LINK_TEXT, "Remove Product").click()

        # switch to the alert
        alert = self.driver.switch_to.alert()

        # get the text from alert
        alert_text = alert.text

        # check alert text
        self.assertEqual("Are you sure you want to remove this item from your Compare Products list?", 
                          alert_text)

        # click on Ok button
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
