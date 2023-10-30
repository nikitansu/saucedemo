from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time


from pages.login_page import Login_page


def test_open_page():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    open = Login_page(driver)
    open.open_page()

    print("Finish test")
    time.sleep(4)
    driver.quit()

