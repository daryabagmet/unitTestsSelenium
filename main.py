import unittest
from HTMLTestRunner.runner import HTMLTestRunner
import os

from HomePage import HomePageTest
from CityPage import CityPageTest
from HotelPage import HotelPageTest


# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class

home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
city_page_test = unittest.TestLoader().loadTestsFromTestCase(CityPageTest)
hotel_page_test = unittest.TestLoader().loadTestsFromTestCase(HotelPageTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, city_page_test, hotel_page_test])

# open the report file
outfile = open(dir + "/SeleniumPythonTestSummary.html", "w")
print(f'outfile: {outfile}')

# # configure HTMLTestRunner options
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report', open_in_browser=True, description="HTMLTestReport", tested_by="Bahmet D", add_traceback=True)
# # run the suite using HTMLTestRunner
runner.run(test_suite)
