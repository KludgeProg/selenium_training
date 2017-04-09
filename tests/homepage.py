import HtmlTestRunner
import os
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a new session
        drivers_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'drivers'))

        # Select the Driver
        driver_selection = input("Which browser you need to test with? (ch, ff, ie)? ")

        if driver_selection == "ff":
            cls.driver = webdriver.Firefox(executable_path='%s\%s' % (drivers_folder, 'geckodriver.exe'))
        elif driver_selection == "ie":
            cls.driver = webdriver.Ie(executable_path='%s\%s' % (drivers_folder, 'iedriverserver.exe'))
        else:
            cls.driver = webdriver.Chrome(executable_path='%s\%s' % (drivers_folder, 'chromedriver.exe'))

        # Create new Session
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # Navigate to the application homepage
        cls.driver.get("https://www.ebay.com/")
        cls.title = cls.driver.title

    def test_search_field(self):
        """ Locating Search Field """
        # Check search field exists on HomePage
        self.assertTrue(self.is_element_present(By.NAME, "_nkw"))

    def test_language_option(self):
        """ Locating Language Option """
        # Check language options dropdown on Homepage
        self.assertTrue(self.is_element_present(By.ID, "gh-eb-Geo"))

    def test_shopping_cart_empty_message(self):
        """ Checking Shopping Cart is Empty """
        # Check content of My Shopping Cart block on Homepage
        shopping_cart_icon = self.driver.find_element_by_css_selector("li#gh-cart")
        shopping_cart_icon.click()

        shopping_cart_status = self.driver.find_element_by_css_selector("div.fw-b").text
        self.assertEqual("Tu carro de compras está vacío, pero no tiene por qué estarlo.", shopping_cart_status)

        # close_button = self.driver.find_element_by_css_selector("a#msgClose")
        # close_button.click()
        # time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Ebay Homepage Test'))
