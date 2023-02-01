import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class FindByLinkText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://courses.letskodeit.com/practice')
        self.driver.implicitly_wait(10) 
        
    def test(self):
        driver = self.driver
        try:
            elementByLinkText = driver.find_element(By.LINK_TEXT, "HOME")
            if elementByLinkText is not None:
                print("Element Found -> By Link Text")
        except NoSuchElementException:
            print('Element Not Found -> By Link Text')
            
        try:
            elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
            if elementByPartialLinkText is not None:
                print("Element Found -> By Partial Link Text")
        except NoSuchElementException:
            print('Element Not Found -> By Partial Link Text')

if __name__ == "__main__":
    unittest.main(verbosity=2)
    run_tests = FindByLinkText()
    run_tests.test()
