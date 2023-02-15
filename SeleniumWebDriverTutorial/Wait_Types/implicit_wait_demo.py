from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class ImplicitWaitDemo(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://courses.letskodeit.com"
        
    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        login_link = driver.find_element(By.XPATH, "//a[text()='Sign In']")
        login_link.click()

        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("test")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)