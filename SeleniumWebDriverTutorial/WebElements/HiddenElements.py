from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

class HiddenElements(unittest.TestCase):
    def setUp(self):
        print("In method: " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://courses.letskodeit.com/practice"

    def testLetsKodeIt(self):
        driver = self.driver
        driver.get(self.base_url)

        # Find the state of the text box
        text_box_element = driver.find_element(By.ID, "displayed-text")
        text_box_state = text_box_element.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(text_box_state))
        time.sleep(2)

        # Click the Hide button
        driver.find_element(By.ID, "hide-textbox").click()
        # Find the state of the text box
        text_box_state = text_box_element.is_displayed()
        print("Text is visible? " + str(text_box_state))
        time.sleep(2)

        # Added code to scroll up because the element was hiding behind the top navigation menu
	    # You will learn about scrolling in future lecture
        driver.execute_script("window.scrollBy(0, -150);")
        # Click the Show button
        driver.find_element(By.ID, "show-textbox").click()
        # Find the state of the text box
        text_box_state = text_box_element.is_displayed()
        print("Text is visible? " + str(text_box_state))
        time.sleep(2)
        # Browser Close
        driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)