from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager

options = Options()
driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))

options.add_argument('--headless')

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
login_standard_user = "standard_user"
password_all="secret_sauce"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('click button')
# text_Products = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_Products = text_Products.text
# print(value_text_Products)
# assert value_text_Products == "Products"
# print("good")

url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
print(get_url)

assert url == get_url
print('good')