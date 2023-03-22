from base import BasePage
from base import InvalidPageException
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    _home_page_promo_locator = 'a.block-promo.home-pants:nth-child(1) > img:nth-child(1)'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.\
                find_element(By.CLASS_NAME, self._home_page_slideshow_locator)
        except:
            raise InvalidPageException("Home Page not loaded")
