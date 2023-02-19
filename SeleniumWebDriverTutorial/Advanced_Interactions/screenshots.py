from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class Screenshots(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://courses.letskodeit.com/"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
        driver.find_element(By.ID, "email").send_keys("abc@email.com")
        driver.find_element(By.ID, "password").send_keys("abc")
        driver.find_element(By.ID, "login").click()
        destinationFileName = "C:\\Users\\adszyman\\Desktop\\NOKIA_COURSES\\MENTOR\\Python\\selenium\\SeleniumWebDriverTutorial\\Advanced_Interactions\\test.png"

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)