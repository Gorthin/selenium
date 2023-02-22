from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest

class DragAndDrop(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://jqueryui.com/droppable/"

    def test_drag_and_drop(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.switch_to.frame(0)

        from_element = driver.find_element(By.ID, "draggable")
        to_element = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(from_element, to_element).perform()            
            print("Drag And Drop Element Successful")
            time.sleep(2)
        except:
            print("Drag And Drop failed on element")


    def test_click_hold_move_release(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.switch_to.frame(0)

        from_element = driver.find_element(By.ID, "draggable")
        to_element = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.click_and_hold(from_element).move_to_element(to_element).release().perform()
            print("Drag And Drop Element Successful")
            time.sleep(2)
        except:
            print("Drag And Drop failed on element")


    def test_drag_and_drop_by_offset(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.switch_to.frame(0)

        from_element = driver.find_element(By.ID, "draggable")
        to_element = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.click_and_hold(from_element).move_to_element_with_offset(to_element, xoffset=15, yoffset=15).release().perform()
            print("Drag And Drop Element Successful")
            time.sleep(2)
        except:
            print("Drag And Drop failed on element")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)