from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class GetText(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        open_tab_element = driver.find_element(By.ID, "opentab")
        element_text = open_tab_element.text
        print("Text on element is: " + element_text)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)