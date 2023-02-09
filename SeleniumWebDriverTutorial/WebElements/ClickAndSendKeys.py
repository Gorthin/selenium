from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class ClickAndSendKeys(unittest.TestCase):
    def setUp(self):
        print("In method: " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        login_link = driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']//a[@href='/login']")
        login_link.click()

        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("test")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("test")

        time.sleep(3)

        email_field.clear()

        time.sleep(3)

        email_field.send_keys("test")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)