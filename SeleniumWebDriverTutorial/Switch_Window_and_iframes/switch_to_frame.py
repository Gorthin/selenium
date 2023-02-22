from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class SwitchToFrame(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://courses.letskodeit.com/practice"
        self.search = "//input[@id='search']"

    def test_frame_id(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using Id
        driver.switch_to.frame("courses-iframe")

        time.sleep(2)
        # Search course
        search_box = driver.find_element(By.XPATH, self.search)
        search_box.send_keys("python")
        time.sleep(2)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")
        time.sleep(1)

    def test_frame_name(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using name
        driver.switch_to.frame("iframe-name")

        time.sleep(2)
        # Search course
        search_box = driver.find_element(By.XPATH, self.search)
        search_box.send_keys("python")
        time.sleep(2)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")
        time.sleep(1)

    def test_frame_num(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using numbers
        driver.switch_to.frame(0)

        time.sleep(2)
        # Search course
        search_box = driver.find_element(By.XPATH, self.search)
        search_box.send_keys("python")
        time.sleep(2)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)