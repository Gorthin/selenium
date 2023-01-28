import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
        
    def test_search_in_python_org_2(self):
        driver = self.driver
        driver.get("http://skleptest.pl/")
        self.assertIn("Generic Shop", driver.title)
        elem = driver.find_element(By.XPATH, '//*[@id="search-field-top-bar"]')
        elem.send_keys("top")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("SEARCH RESULTS FOR: TOP.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()