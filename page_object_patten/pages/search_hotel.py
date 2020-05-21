class SearchHotelPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_span_xpath = "//span[text() ='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id = 'select2-drop']//input"
        self.location_match_span_xpath = "//span[text()='Dubai']"
        self.check_in_input_name = 'checkin'
        self.check_out_input_name = 'checkout'
        self.travellers_input_name = 'travellers'
        self.child_input_id = 'childInput'
        self.search_button_xpah = "//button[text()=' Search']"

    def set_city(self,city):
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_span_xpath).click()

    def set_dater_range(self, check_in, check_out):
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in)
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_out)

    def set_travellers(self,child):
        self.driver.find_element_by_name(self.travellers_input_name).clear()
        self.driver.find_element_by_name(self.travellers_input_name).send_keys(child)

    def perform_search(self):
        self.driver.find_element_by_xpath(self.search_button_xpah).click()