import unittest
from search_product import SearchTest
from homepage import HomePageTest

# Get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# Run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
