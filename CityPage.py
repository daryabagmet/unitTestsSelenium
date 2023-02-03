import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class CityPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(20)
        inst.driver.maximize_window()

        inst.driver.get("https://www.agoda.com/uk-ua/")

        button_cookie = inst.driver.find_element(By.XPATH, "//button[@data-element-name = 'consent-banner-accept-btn']")
        button_cookie.click()

    def test_search_results(self):
        self.setUpClass()

        search_field = self.driver.find_element(By.ID, "textInput")
        search_field.send_keys("Rome")
        search_button = self.driver.find_element(By.XPATH, "//button[@data-selenium='searchButton']")
        search_button.click()
        self.assertTrue(self.is_results_found(), "No results found.")
        

    def test_search_no_results(self):        
        search_field = self.driver.find_element(By.ID, "textInput")
        search_field.send_keys("dh238!")
        search_button = self.driver.find_element(By.XPATH, "//button[@data-selenium='searchButton']")
        search_button.click()
        self.assertEqual(0, self.is_no_results_found())

    @classmethod

    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

    def is_results_found(self):
      # Search for list of results
      try:
        hotels_list = self.driver.find_element(By.CLASS_NAME, "hotel-list-container")
        hotels_list_items = hotels_list.find_elements(By.CSS_SELECTOR, "li.PropertyCardItem")

      finally:
        return hotels_list_items if len(hotels_list_items) else 0

    def is_no_results_found(self):
      # Search for list of results
        results_list = self.driver.find_element(By.CLASS_NAME, "InterstitialList")
        results_list_items = results_list.find_elements(By.TAG_NAME, "li")

        return len(results_list_items)

if __name__ == '__main__':
    unittest.main()
