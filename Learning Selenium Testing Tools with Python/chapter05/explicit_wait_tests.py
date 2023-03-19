from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest


class ExplicitWaitTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo-magento-2.auroracreation.com/")

    def test_account_link(self):
        WebDriverWait(self.driver, 10)\
            .until(lambda s: s.find_element(By.ID, "switcher-language-trigger").get_attribute("tabindex") == "0")

        account = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Utwórz konto")))
        account.click()

    def test_create_new_customer(self):
        # click on Log In link to open Login page
        self.driver.find_element(By.LINK_TEXT, "Utwórz konto").click()

        # wait for My Account link in Menu
        my_account = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Utwórz konto")))
        my_account.click()

        # get the Create Account button
        create_account_button = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Utwórz konto")))

        # click on Create Account button. This will displayed new account
        create_account_button.click()
        WebDriverWait(self.driver, 10)\
            .until(expected_conditions.title_contains("Utwórz nowe konto klienta"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
