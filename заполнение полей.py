from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# user_name = driver.find_element_by_id("user-name")
user_name = driver.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")