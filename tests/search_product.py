import HtmlTestRunner
import os
import time
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.title = cls.driver.title

    def test_search_by_category(self):
        """ Searching Product by Category """
        # Click on Search Button
        self.search_button = self.driver.find_element_by_class_name("search")
        self.search_button.click()

        # Get the search textbox
        self.search_field = self.driver.find_element_by_name("keys")
        self.search_field.clear()

        # Enter search keyword and Submit
        self.search_field.send_keys("phones")
        self.search_field.submit()
        time.sleep(5)

        # Get Products Link
        self.products_link = self.driver.find_element_by_link_text("products")
        self.products_link.click()
        time.sleep(5)

        # Get all the anchor elements which have product names displayed currently on result page using
        # xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='result-title']/a")
        self.assertEqual(1, len(products))
        self.assertNotEqual(products[0].text, "")

    def test_search_by_name(self):
        """ Searching Product by Name """
        # Get the search textbox
        self.search_field = self.driver.find_element_by_name("keys")
        self.search_field.clear()

        # Enter search keyword and Submit
        self.search_field.send_keys("salt shaker")
        self.search_field.submit()
        time.sleep(5)

        # Get Products Link
        self.products_link = self.driver.find_element_by_link_text("products")
        self.products_link.click()
        time.sleep(5)

        # Get all the anchor elements which have product names displayed currently on result page using
        # xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='result-title']/a")
        self.assertEqual(1, len(products))

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Search Product Test'))
