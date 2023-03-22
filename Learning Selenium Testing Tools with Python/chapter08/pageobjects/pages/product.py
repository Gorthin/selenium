from base import BasePage
from base import InvalidPageException
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    _product_view_locator = 'div.search.results:nth-child(5)'
    _product_name_locator = 'a.product-item-link'
    _product_list_locator = 'ol.products.list.items.product-items'
    _product_stock_status_locator = '#toolbar-amount'
    _product_price_locator = '#min-product-price-53'

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    @property
    def name(self):
        return self.driver.\
            find_element(By.CSS_SELECTOR, self._product_name_locator)\
            .text.strip()

    @property
    def description(self):
        return self.driver.\
            find_element(By.CSS_SELECTOR, self._product_list_locator)\
            .text.strip()

    @property
    def stock_status(self):
        return self.driver.\
            find_element(By.CSS_SELECTOR, self._product_stock_status_locator)\
            .text.strip()

    @property
    def price(self):
        return self.driver.\
            find_element(By.CSS_SELECTOR, self._product_price_locator)\
            .text.strip()

    def _validate_page(self, driver):
        try:
            driver.find_element(By.CSS_SELECTOR, self._product_view_locator)
        except:
            raise InvalidPageException('Product page not loaded')
