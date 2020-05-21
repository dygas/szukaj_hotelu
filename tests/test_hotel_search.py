import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_patten.pages.search_hotel import SearchHotelPage


class TestHotelSearch:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait()
        self.driver.maximize_window()
        yield


    def test_hotel_search(self,setup):
        self.driver.get('http://www.kurs-selenium.pl/demo/')
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city('Dubai')
        search_hotel_page.set_dater_range('19/06/2020', '20/06/2020')
        search_hotel_page.set_travellers('2')
        search_hotel_page.perform_search()
