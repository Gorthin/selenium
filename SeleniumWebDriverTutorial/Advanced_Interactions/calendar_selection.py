from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class CalendarSelection(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.base_url = "http://www.expedia.com"
        self.driver.implicitly_wait(3)

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        # Click flights tab
        driver.find_element(By.XPATH, "//span[contains(text(),'Flights')]").click()
        one_way = driver.find_element(By.XPATH, "//span[contains(text(),'One-way')]")
        one_way.click()
        # Click departing field
        driver.find_element(By.ID, "d1-btn").click()
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        calMonth = driver.find_element(By.XPATH, "//div[@class='uitk-date-picker-menu-months-container']/div[1]/table[1]/tbody[1]")
        allValidDates = calMonth.find_elements(By.TAG_NAME, "button")
        
        time.sleep(2)

        for date in allValidDates:
            if date.get_attribute('data-day') == "30":
                date.click()
                break

            
        btn_done = driver.find_element(By.XPATH, "//div[@class='uitk-layout-flex-item uitk-layout-flex-item-flex-shrink-0 dialog-done']//button[@type='button'][contains(text(),'Done')]")
        btn_done.click()
        time.sleep(2)
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)