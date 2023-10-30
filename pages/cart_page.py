from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_checkout = '//button[@class="btn btn_action btn_medium checkout_button "]'



    # Getters
    def get_button_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))


    # Actions
    def click_button_checkout(self):
        self.get_button_checkout().click()
        print("Click Button Checkout")


    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_button_checkout()