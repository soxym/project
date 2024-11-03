import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.maximize_window()
# message = "hello"
# input_pole = driver.find_element(By.XPATH, "//input[@id='user-message']")
# input_pole.send_keys(message)
# print('input_pole')
#
#
# click_button = driver.find_element(By.XPATH, "//button[@id='showInput']")
# click_button.click()
# print(click_button)
#
# pole_message = driver.find_element(By.XPATH, "//p[@id='message']")
# value_pole_message = pole_message.text
# print(value_pole_message)
# assert value_pole_message == message
# print("значения верны")

num_1 = 123
num_2 = 102
input_pole_1 = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_pole_1.send_keys(num_1)
print('input_pole_1')
time.sleep(3)
input_pole_2 = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_pole_2.send_keys(num_2)
print('input_pole_2')
time.sleep(3)
click_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Get Sum')]")
click_button.click()
print(click_button)
time.sleep(3)
pole_sum = driver.find_element(By.XPATH, "//p[@id='addmessage']")
value_pole_sum = pole_sum.text
print(value_pole_sum)
sum = num_1+num_2
assert value_pole_sum == str(sum)
print("значения верны")

