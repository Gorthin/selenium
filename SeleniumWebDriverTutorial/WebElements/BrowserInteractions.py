import unittest
from selenium import webdriver

class BrowserInteractions(unittest.TestCase):
    def setUp(self):
        print("In method " + str(self._testMethodName))
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://courses.letskodeit.com/practice"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)
        # Get Current Url
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")
        # Open another Url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1")
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Get Page Source
        page_source = driver.page_source
        print(page_source)
        # Browser Close / Quit
        # driver.close()
        driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)