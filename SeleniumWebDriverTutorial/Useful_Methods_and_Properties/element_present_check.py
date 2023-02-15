from selenium import webdriver
from selenium.webdriver.common.by import By
from handy_wrappers import HandyWrappers
import unittest


class ElementPresentCheck(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.hw = HandyWrappers(self.driver)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)
        hw = HandyWrappers(self.driver)
        
        element_result_1 = hw.is_element_present("name", By.ID)
        print(str(element_result_1))

        element_result_2 = hw.element_presence_check("//input[@id='name1']", By.XPATH)
        print(str(element_result_2))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)