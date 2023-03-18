import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class NavigationTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://www.google.com")

    def test_browser_navigation(self):
        driver = self.driver
        # get the search textbox
        search_field = driver.find_element(By.NAME, "q")
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys("selenium webdriver")
        search_field.submit()

        se_wd_link = driver.\
            find_element(By.LINK_TEXT, "Selenium WebDriver")
        se_wd_link.click()
        self.assertEqual("WebDriver | Selenium", driver.title)

        driver.back()
        self.assertTrue(WebDriverWait(self.driver, 10)
            .until(expected_conditions.title_is("selenium webdriver - Google Search")))

        driver.forward()
        self.assertTrue(WebDriverWait(self.driver, 10)
            .until(expected_conditions.title_is("WebDriver | Selenium")))

        driver.refresh()
        self.assertTrue(WebDriverWait(self.driver, 10)
            .until(expected_conditions.title_is("WebDriver | Selenium")))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
