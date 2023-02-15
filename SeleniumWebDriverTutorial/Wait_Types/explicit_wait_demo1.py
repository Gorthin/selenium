from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import unittest


class ExplicitWaitDemo1(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.base_url = "https://courses.letskodeit.com/"
        
    def test(self):
        driver = self.driver
        # driver.get(self.base_url)
        driver.execute_script("window.location = 'https://courses.letskodeit.com/';")
        # driver.find_element(By.XPATH, "//a[text()='Sign In']").click()

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                                                ignored_exceptions=[NoSuchElementException,
                                                                    ElementNotVisibleException,
                                                                    ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sign In']")))
        element.click()

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
