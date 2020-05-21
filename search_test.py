from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(20)
driver.maximize_window()
driver.get('http://www.kurs-selenium.pl/demo/')
driver.find_element_by_xpath("//span[text() ='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id = 'select2-drop']//input").send_keys('Dubai')
driver.find_element_by_xpath("//span[text()='Dubai']").click()
driver.find_element_by_name('checkin').send_keys('16/06/2020')
driver.find_element_by_name('checkout').send_keys('17/06/2020')
driver.find_element_by_name('travellers').click()
driver.find_element_by_id('childInput').clear()
driver.find_element_by_id('childInput').send_keys('1')
driver.find_element_by_xpath("//button[text()=' Search']").click()
hotels = driver.find_elements_by_xpath("//h4[contains(@class,'list_title')]//b")
hotel_names =[hotel.get_attribute('texContent') for hotel in hotels]
#for name in hotel_names:
    #print(name)

prices = driver.find_elements_by_xpath("//div[contains(@class,'price_tab')]//b")
price_values = [price.get_attribute('textContent') for price in prices]
#for price in price_values:
    #print('Cena to : '+ prices)

#assert hotel_names[0] == 'Jumeirah Beach Hotel'
#assert price_values[0] == '$22'
driver.quit()
