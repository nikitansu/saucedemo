from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_1 = '//button[@data-test="add-to-cart-sauce-labs-backpack"]'
    cart = '//a[@class="shopping_cart_link"]'
    menu = '//button[@id="react-burger-menu-btn"]'
    about_button = '//a[@id="about_sidebar_link"]'

    # Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_button)))

    # Actions
    def click_product_1(self):
        self.get_product_1().click()
        print("Click Select Product")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click Menu")

    def click_about_button(self):
        self.get_about_button().click()
        print("Click About Button")

        # Methods

    def select_product_1(self):
        self.get_current_url()
        self.click_product_1()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_about_button()
        self.assert_url('https://saucelabs.com/')
