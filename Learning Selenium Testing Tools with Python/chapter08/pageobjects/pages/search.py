from base import BasePage
from base import InvalidPageException
from product import ProductPage
from selenium.webdriver.common.by import By


class SearchRegion(BasePage):
    _search_box_locator = '#search'

    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchFor(self, term):
        self.search_field = self.driver\
            .find_element(By.NAME, self._search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()
        return SearchResults(self.driver)


class SearchResults(BasePage):
    _product_list_locator = 'ol.products.list.items.product-items'
    _product_name_locator = 'a.product-item-link'
    _product_image_link = 'img.product-image-photo'
    _page_title_locator = 'a.logo > img'
    _products_count = 0
    _products = {}

    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        results = self.driver\
            .find_elements(By.CSS_SELECTOR, self._product_list_locator)
        for product in results:
            name = product\
                .find_element(By.CSS_SELECTOR, self._product_name_locator).text
            self._products[name] = product\
                .find_element(By.CSS_SELECTOR, self._product_image_link)

    def _validate_page(self, driver):
        if 'Search results for' not in driver.title:
            raise InvalidPageException('Search results not loaded')

    @property
    def product_count(self):
        return len(self._products)

    def get_products(self):
        return self._products

    def open_product_page(self, product_name):
        self._products[product_name].click()
        return ProductPage(self.driver)
