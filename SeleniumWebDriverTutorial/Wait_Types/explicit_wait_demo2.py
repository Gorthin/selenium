from selenium import webdriver
from explicit_wait_type import ExplicitWaitType
import time
import unittest


class ExplicitWaitDemo2(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.base_url = "https://courses.letskodeit.com/"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        wait = ExplicitWaitType(driver)
        element = wait.wait_for_element(locator="//a[text()='Sign In']", locator_type="xpath")
        element.click()

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)