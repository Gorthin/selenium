from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class DynamicXPathFormat(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://courses.letskodeit.com/"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, "//a[contains(text(),'ALL COURSES')]").click()

        search_box = driver.find_element(By.XPATH, "//input[@id='search']")
        search_box.send_keys("JavaScript")
        btn_search = driver.find_element(By.XPATH, "//button[@type='submit']")
        btn_search.click()

        course_element = driver.find_element(By.XPATH, "//h4[@class='dynamic-heading']")
        course_element.click()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)