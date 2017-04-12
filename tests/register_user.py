import HtmlTestRunner
import time
import unittest
from helper.constants import drivers_folder
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path='%s\%s' % (drivers_folder, 'geckodriver.exe'))
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # Navigate to the application homepage
        cls.driver.get('https://www.ebay.com')

    def test_register_new_user(self):
        """ Testing for Sign Up """
        # Click on Log In link to open Login Page
        self.driver.find_element_by_link_text("Inicia sesión").click()
        # Get the Create Account Button
        create_account_span = self.driver.find_element_by_xpath("//span[.='Regístrate']")
        # Checking the Span is displayed and enabled
        self.assertTrue(create_account_span.is_displayed() and create_account_span.is_enabled())
        # Click on Create Account Span. This will display new account
        create_account_span.click()
        # Check title
        registration_button = self.driver.find_element_by_xpath("//button[@id='sbtBtn']")
        self.assertEquals("Regístrate", registration_button.text)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # Close the Browser Window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Ebay Selectors Test'))
