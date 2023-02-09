from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class WorkingWithElementsList(unittest.TestCase):
    def setUp(self):
        print("In method: " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://courses.letskodeit.com/practice"

    def testListOfElements(self):
        driver = self.driver
        driver.get(self.base_url)

        radio_buttons_list = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radio_buttons_list)
        print("Size of the list: " + str(size))

        for radio_button in radio_buttons_list:
            is_selected = radio_button.is_selected()

            if not is_selected:
                radio_button.click()
                time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)