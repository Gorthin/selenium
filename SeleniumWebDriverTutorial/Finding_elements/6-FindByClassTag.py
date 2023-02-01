import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class FindByClassTag(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://courses.letskodeit.com/practice')
        self.driver.implicitly_wait(10)
        
    def test(self):
        driver = self.driver
        try:
            elementByClassName = driver.find_element(By.CLASS_NAME, "inputs")

            if elementByClassName is not None:
                print("Element Found -> By Class Name")
                elementByClassName.send_keys("Testing")
        except NoSuchElementException:
            print('Element Not Found -> By Id')
            
        try:
            elementByTagName = driver.find_element(By.TAG_NAME, "a")

            if elementByTagName is not None:
                print("Element Found -> By Tag Name: " + elementByTagName.text)
                
            # time.sleep(5)
        except NoSuchElementException:
            print('Element Not Found -> By Id')
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    run_tests = FindByClassTag()
    run_tests.test()