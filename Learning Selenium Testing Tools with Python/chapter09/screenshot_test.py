from selenium import webdriver
import datetime, time, unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ScreenShotTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://magento2-demo.magebit.com/")

    def test_screen_shot(self):
        driver = self.driver
        try:
            promo_banner_elem = driver.find_element(By.XPATH, "//img[@src='https://magento2-demo.magebit.com/media/wysiwyg/home/home-main.jpg']")
            self.assertNotEqual("Promotions", promo_banner_elem.text)
        except NoSuchElementException:
            st = datetime.datetime\
                .fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
            file_name = "main_page_missing_banner" + st + ".png"
            driver.save_screenshot(file_name)
            raise

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
