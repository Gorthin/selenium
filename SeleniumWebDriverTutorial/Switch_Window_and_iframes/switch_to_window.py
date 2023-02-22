from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class SwitchToWindow(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        # Find parent handle -> Main Window
        parent_handle = driver.current_window_handle
        print("Parent Handle: " + parent_handle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                search_box = driver.find_element(By.XPATH, "//input[@id='search']")
                search_box.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parent_handle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)