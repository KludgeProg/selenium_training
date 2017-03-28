import os
import time
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    def setUp(self):
        drivers_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'drivers'))

        # Select the Driver
        driver_selection = input("Which browser you need to test with? (ch, ff, ie)? ")

        if driver_selection == "ff":
            self.driver = webdriver.Firefox(executable_path='%s\%s' % (drivers_folder, 'geckodriver.exe'))
        elif driver_selection == "ie":
            self.driver = webdriver.Ie(executable_path='%s\%s' % (drivers_folder, 'iedriverserver.exe'))
        else:
            self.driver = webdriver.Chrome(executable_path='%s\%s' % (drivers_folder, 'chromedriver.exe'))

        # Create new Session
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # Navigate to the application homepage
        self.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_category(self):
        # Click on Search Button
        self.search_button = self.driver.find_element_by_class_name("search")
        self.search_button.click()

        # Get the search textbox
        self.search_field = self.driver.find_element_by_name("keys")
        self.search_field.clear()

        # Enter search keyword and Submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # Get Products Link
        self.products_link = self.driver.find_element_by_link_text("products")
        self.products_link.click()

        # Wait until page reloads javascript || jQuery
        time.sleep(5)

        # Get all the anchor elements which have product names displayed currently on result page using
        # xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='result-title']/a")
        self.assertEqual(1, len(products))

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
