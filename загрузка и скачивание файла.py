import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.maximize_window()
time.sleep(5)
path_upload = "C:\\Users\\User\\PycharmSelenium\\pythonProject\\screen\\screenshot 2024.10.10-17.02.35.png"
button_login = driver.find_element(By.XPATH, "//input[@id='file']")
button_login.send_keys(path_upload)
print('click button')