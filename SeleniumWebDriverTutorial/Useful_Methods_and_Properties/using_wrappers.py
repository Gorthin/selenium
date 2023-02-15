from selenium import webdriver
from handy_wrappers import HandyWrappers
import time
import unittest


class UsingWrappers(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.hw = HandyWrappers(self.driver)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)
        hw = HandyWrappers(self.driver)

        text_field_1 = hw.get_element("name")
        text_field_1.send_keys("Test")
        time.sleep(2)
        text_field_2 = hw.get_element("//input[@id='name']", locator_type="xpath")
        text_field_2.clear()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)