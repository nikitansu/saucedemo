from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = '//input[@placeholder="First Name"]'
    last_name = '//input[@placeholder="Last Name"]'
    postal_code = '//input[@placeholder="Zip/Postal Code"]'
    button_continue = '//input[@type="submit"]'

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))


    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First Name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input Last Name')

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print('Input Postal Code')

    def click_button_continue(self):
        self.get_button_continue().click()
        print('Tap Login Continue')

    # Methods
    def filling_client_information(self):
        self.get_current_url()
        self.input_first_name("First Name")
        self.input_last_name("Last Name")
        self.input_postal_code("123456")
        self.click_button_continue()
