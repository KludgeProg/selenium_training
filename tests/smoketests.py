import HtmlTestRunner
import os
import unittest
from homepage import HomePageTest
from search_product import SearchTest

# Get the directory path to output report file
dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\reports"

# Get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# Open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")

# Configure the HtmlTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(
    stream=outfile, report_title='Test Report', descriptions='Smoke Tests', output='Test Report'
)

# Run the suite
runner.run(smoke_tests)
