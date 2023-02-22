from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest

class MouseHovering(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test_top(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//button[@id='mousehover']")
        item_to_click_locator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            top_link = driver.find_element(By.XPATH, item_to_click_locator)
            actions.move_to_element(top_link).click().perform()
            print("Item Clicked")
            time.sleep(2)
        except:
            print("Mouse Hover failed on element")

    def test_reload(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//button[@id='mousehover']")
        item_to_click_locator = ".//div[@class='mouse-hover-content']//a[text()='Reload']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            top_link = driver.find_element(By.XPATH, item_to_click_locator)
            actions.move_to_element(top_link).click().perform()
            print("Item Clicked")
            time.sleep(4)
        except:
            print("Mouse Hover failed on element")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)