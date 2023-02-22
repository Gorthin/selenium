from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest

class Sliders(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://jqueryui.com/slider/"

    def test_slider(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding Element Successful")
            time.sleep(2)
        except:
            print("Sliding failed on element")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)