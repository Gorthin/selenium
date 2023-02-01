import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class FindByXPathCSS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://courses.letskodeit.com/practice')
        self.driver.implicitly_wait(10)
    
    def test(self):
        driver = self.driver
        try:
            element_by_xpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
            if element_by_xpath is not None:
                print("Element Found -> By XPath")
        except NoSuchElementException:
            print('Element Not Found -> By XPath')

        try:
            element_by_css = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
            if element_by_css is not None:
                print("Element Found -> By CSS")
        except NoSuchElementException:
            print('Element Not Found -> By CSS')
        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    run_tests = FindByXPathCSS()
    run_tests.test()