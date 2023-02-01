import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ListOfElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://courses.letskodeit.com/practice')
        self.driver.implicitly_wait(10) 

    def test(self):
        driver = self.driver

        elementListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")
        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("ClassName -> Size of the list is: " + str(length1))
        self.assertEqual(length1, 3)

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("TagName -> Size of the list is: " + str(length2))
        self.assertEqual(length2, 9)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    run_tests = ListOfElements()
    run_tests.test()
