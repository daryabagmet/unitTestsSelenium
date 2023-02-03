import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class HotelPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(20)
        inst.driver.maximize_window()

        inst.driver.get("https://www.agoda.com/uk-ua/")
        #close cookie message
        button_cookie = inst.driver.find_element(By.XPATH, "//button[@data-element-name = 'consent-banner-accept-btn']")
        button_cookie.click()

    def test_hotel_page(self):
        wait = WebDriverWait(self.driver, 20)
        #search hotels in city
        search_field = self.driver.find_element(By.ID, "textInput")
        search_field.send_keys("Kyiv")
        search_button = self.driver.find_element(By.XPATH, "//button[@data-selenium='searchButton']")
        search_button.click()
        #close banner
        banner = wait.until(
          EC.presence_of_element_located((By.CLASS_NAME, "ab-in-app-message"))
        )

        banner_close_button = banner.find_element(By.CLASS_NAME,"ab-close-button")
        banner_close_button.click()

        hotels_list = wait.until(
          EC.presence_of_element_located((By.CLASS_NAME, "hotel-list-container"))
        )

        hotels_list_items = hotels_list.find_elements(By.CSS_SELECTOR, "li.PropertyCardItem")
        #get the first hotel from results list
        first_item = hotels_list_items[0]
       
        hotels_items_container = first_item.find_element(By.XPATH, "//div[@data-selenium='selectedHotelContainer']")
        hotels_item_link = hotels_items_container.find_element(By.XPATH, "//a[@data-element-index='0']")
        hotel_page_link = hotels_item_link.get_attribute("href")
        #navigate to hotel page
        self.driver.get(hotel_page_link)
        #check the main blocks
        self.assertTrue(self.is_element_present(By.ID,"SearchBoxContainer"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"div.Mosaic"))
        self.assertTrue(self.is_element_present(By.XPATH,"//div[@data-element-name='property-short-description']"))
        self.assertTrue(self.is_element_present(By.ID,"roomGridContent"))

        hotel_page_results = self.driver.find_elements(By.CSS_SELECTOR, "div.MasterRoom")
        #get the first room
        first_room = hotel_page_results[0]
        hotel_room_book = first_room.find_element(By.XPATH, "//button[@ data-selenium='ChildRoomsList-bookButtonInput']")
        hotel_room_book.click()
        #navigate to contact details page
        self.driver.implicitly_wait(30)
        #check the guest details block on contact details page
        self.assertTrue(self.is_element_present(By.XPATH,"//div[@data-component='GuestDetailsComponent']"))

    @classmethod

    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

    def is_element_present(self, how, what):
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException: 
            return False
        return True

if __name__ == '__main__':
    unittest.main()
