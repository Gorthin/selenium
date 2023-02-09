from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class DropdownSelect(unittest.TestCase):
    def setUp(self):
        print("In method: " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
