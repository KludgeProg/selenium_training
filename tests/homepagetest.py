import HtmlTestRunner
import unittest
from helpers.constants import firefox_driver


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a new Firefox Session
        cls.driver = firefox_driver
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # Navigate to the application home page
        cls.driver.get('https://www.ebay.com')

    def test_search_text_field_max_length(self):
        """ Looking for MaxLength of Search Field """
        # Get the search Textbox
        search_field = self.driver.find_element_by_id("gh-ac")
        # Check Maxlength attribute is set to 128
        self.assertEqual("300", search_field.get_attribute("maxlength"))

    def test_search_button_enabled(self):
        """ Looking if Search Button is Enabled """
        # Get Search Button
        search_button = self.driver.find_element_by_class_name("btn-prim")
        # Check Search Button is enabled
        self.assertTrue(search_button.is_enabled())

    def test_my_account_link_is_displayed(self):
        """ Checking Register Links """
        # Get the Register Link
        registration_link = self.driver.find_element_by_link_text("Registro")
        # Check Register Link is displayed/visible in the Homepage Footer
        self.assertTrue(registration_link.is_displayed())

    def test_account_links(self):
        """ Getting Mi eBay account Links"""
        # Get all the links with Mi eBay text in it
        account_links = self.driver.find_elements_by_partial_link_text("Mi eBay")
        # Check Mi eBay Links are displayed / visible in the Homepage
        self.assertTrue(2, len(account_links))

    def test_count_of_promo_banners_images(self):
        """ Counting Visible Promo Images on Homepage """
        # Get promo banner list
        banner_list = self.driver.find_element_by_class_name("horizontal-daily-deals")
        # Get images from the banner_list
        banners = banner_list.find_elements_by_tag_name("img")
        # Check there are 25 banners displayed on the page
        self.assertEqual(25, len(banners))

    def test_image_go_to_section(self):
        """ Checking for Image and section """
        # Get Image by Xpath
        xpath_image = self.driver.find_element_by_xpath("//img[@alt='']")
        # Check image is displayed on homepage
        self.assertTrue(xpath_image.is_displayed())
        # Click on image to open the page
        xpath_image.click()
        # Check page Title
        self.assertEqual("Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay", self.driver.title)

    def test_shopping_cart_status(self):
        """ Check content of My Shopping Cart Block on Homepage """
        # Get the Shopping Cart Icon and Click to open the Shopping Cart Section
        shopping_cart_icon = self.driver.find_element_by_css_selector("li#gh-cart")
        shopping_cart_icon.click()
        # Get the shopping cart status
        shopping_cart_status = self.driver.find_element_by_css_selector("div.fw-b").text
        self.assertEqual("Tu carro de compras está vacío, pero no tiene por qué estarlo.", shopping_cart_status)

    @classmethod
    def tearDownClass(cls):
        # Close the Browser Window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Ebay Selectors Test'))

