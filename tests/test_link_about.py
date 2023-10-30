import time

from selenium import webdriver
from pages.login_page import Login_page
from pages.main_page import Main_page

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_link_about():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    print("Start Test")


    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()


    print("Finish Test")
    time.sleep(4)
    driver.quit()






