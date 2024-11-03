import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
login_standard_user = "standard_user"
password_all="secret_sauce"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')
# time.sleep(5)
# user_name.clear()
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('click button')

menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
print('click menu button')
time.sleep(5)
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
print('click about button')

driver.back()
print("go back")
time.sleep(10)
driver.forward()
print("go forward")