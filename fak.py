import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager





from faker import Faker

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
fak = Faker("en_US")
name = fak.first_name() + str(fak.random_int())
passw = fak.password()
print(name)
print(passw)
login_standard_user = "standard_user"
password_all="secret_sauce"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(name)
print('Input Login')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(passw)
print('Input password')