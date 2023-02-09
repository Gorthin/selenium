import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonsAndCheckboxes(unittest.TestCase):
    def setUp(self):
        print("In method: " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test_radio_buttons_and_checkboxes(self):
        driver = self.driver
        driver.get(self.base_url)

        bmw_radio_btn = driver.find_element(By.ID, "bmwradio")
        bmw_radio_btn.click()
        time.sleep(2)
                
        benz_radio_btn = driver.find_element(By.ID,"benzradio")
        benz_radio_btn.click()
        time.sleep(2)
        
        bmw_checkbox = driver.find_element(By.ID,"bmwcheck")
        bmw_checkbox.click()
        time.sleep(2)
        
        benz_checkbox = driver.find_element(By.ID,"benzcheck")
        benz_checkbox.click()
        
        print("BMW Radio button is selected? " + str(bmw_radio_btn.is_selected())) # True if selected, False is not selected
        print("Benz Radio button is selected? " + str(benz_radio_btn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmw_checkbox.is_selected()))
        print("Benz Checkbox is selected? " + str(benz_checkbox.is_selected()))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)