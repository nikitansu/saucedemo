from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Page URL
    url = 'https://www.saucedemo.com/'

    # Locators
    user_name = '//input[@placeholder="Username"]'
    password = '//input[@placeholder="Password"]'
    button_login = '//input[@id="login-button"]'
    main_word = '//span[text()="Products"]'

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input Login")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input Password')

    def click_button_login(self):
        self.get_button_login().click()
        print('Tap Login Button')


    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_button_login()
        self.assert_word(self.get_main_word(), "Products")

