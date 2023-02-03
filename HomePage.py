import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(20)
        inst.driver.maximize_window()

        # navigate to the home page
        inst.driver.get("https://www.agoda.com/uk-ua/")

        # close cookie's banner
        button_cookie = inst.driver.find_element(By.XPATH, "//button[@data-element-name ='consent-banner-accept-btn']")

        button_cookie.click()

    def test_main_info(self):
        # check present main blocks and title on Home page
        self.assertTrue(self.is_title_matches(), "Title doesn't match.")
        self.assertTrue(self.is_element_present(By.ID,"tabpanel-all-rooms-tab"))
        self.assertTrue(self.is_element_present(By.XPATH,"//ul[@role='tablist']"))
        self.assertTrue(self.is_element_present(By.XPATH,"//div[@data-element-name='accommodation-entry-panel']"))
        
    def test_search_request(self):
        # # get search field
        search_field = self.driver.find_element(By.XPATH, "//input[@data-selenium='textInput']")
        # # enter search keyword and submit
        search_field.send_keys("Kyiv")
        search_button = self.driver.find_element(By.XPATH, "//button[@data-selenium='searchButton']")
        search_button.click()

    @classmethod
    def tearDown(inst):
        inst.driver.quit()

    def is_title_matches(self):
        return "Agoda" in self.driver.title

    def is_element_present(self, how, what):
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException: 
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)
