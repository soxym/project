import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
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
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(5)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(5)
# user_name.send_keys('er')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input password')
password.send_keys(Keys.RETURN)
# filter = driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']")
# filter.click()
# print('click filter')
# time.sleep(5)

# option = driver.find_element(By.XPATH, "//option[@value='hilo']").click()
# driver.find_element(By.XPATH, "//option[@value='hilo']").click()
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print('click button')
now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_screenshot = "screenshot " + now_date + ".png"
driver.save_screenshot('C:\\Users\\User\\PycharmSelenium\\pythonProject\\screen\\'+ name_screenshot)
