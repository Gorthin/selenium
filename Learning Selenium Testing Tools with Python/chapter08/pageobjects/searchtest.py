import unittest
from pages.homepage import HomePage
from base.basetestcase import BaseTestCase


class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor('phones')
        self.assertEqual(3, search_results.product_count)
        product = search_results.open_product_page('Luma Mailed Gift Card ')
        self.assertEqual('Luma Mailed Gift Card ', product.name)
        self.assertEqual('$25.00', product.price)
        self.assertEqual('IN STOCK', product.stock_status)

if __name__ == '__main__':
    unittest.main(verbosity=3)
