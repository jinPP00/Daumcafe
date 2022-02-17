import os
from selenium import webdriver


def test_driver():
    chrome_driver = os.path.join('chromedriver')

    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.implicitly_wait(3)
    driver.quit()

    assert driver is not None
