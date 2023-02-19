from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class JavaScriptExecution(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.execute_script("window.location = 'https://courses.letskodeit.com/practice';")
        self.driver.implicitly_wait(3)
        time.sleep(6)

    def test(self):
        driver = self.driver
        
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)