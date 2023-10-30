from selenium import webdriver

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_buy_product():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    print("Start Test")


    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.filling_client_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print("Finish Test")
    time.sleep(3)
    driver.quit()




