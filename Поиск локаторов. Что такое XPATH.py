from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# user_name = driver.find_element(By.ID,"user-name") #ID
# user_name = driver.find_element(By.NAME,"user-name") #NAME
# user_name = driver.find_element(By.XPATH,"//*[@id='user-name']") #Full XPATH
# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #ID XPATH
user_name = driver.find_element(By.XPATH, "//input[@data-test='username']") #data-test XPATH
password = driver.find_element(By.CSS_SELECTOR, "#password") #CSS_SELECTOR
user_name.send_keys("standard_user")
password.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()