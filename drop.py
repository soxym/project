import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# base_url = 'https://www.saucedemo.com/'
# driver.get(base_url)
# driver.maximize_window()
# login_standard_user = "standard_user"
# password_all="secret_sauce"
# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# user_name.send_keys(login_standard_user)
# print('Input Login')
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print('Input password')
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print('click button')
#
# select = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
# time.sleep(5)
# # select.select_by_visible_text('Name (Z to A)')
# select.select_by_value('lohi')

base_url = 'https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.maximize_window()

click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop.click()
print('click_drop')
time.sleep(5)
# click_country = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[4]")
# click_country.click()
# print('click_country')
input_country = driver.find_element(By.XPATH, "(//input[@class='select2-search__field'])[2]")
input_country.send_keys('Denmark')
time.sleep(2)
input_country.send_keys(Keys.RETURN)