import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager


# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# base_url = 'https://demoqa.com/checkbox'
# driver.get(base_url)
# driver.maximize_window()
#
# check_box = driver.find_element(By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']")
# check_box.click()
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
# driver.get(base_url)
# driver.maximize_window()
#
# time.sleep(10)
#
# check_box = driver.find_element(By.XPATH, "//input[@value='cb1']")
# check_box.click()
# print('click check_box')
#
# check_box_2 = driver.find_element(By.XPATH, "//input[@value='cb3']")
# check_box_2.click()
# print('click check_box_2')

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = 'https://fincalculator.ru/kalkulyator-dnej?ysclid=lnbpcpoo7797276405'
driver.get(base_url)
driver.maximize_window()

# action = ActionChains(driver)
#
# double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
#
# action.double_click(double_click_button).perform()    # Вызываем метод двойного клика
#
# print('Произвели двойной клик')
#
# action = ActionChains(driver)
#
# right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
#
# action.context_click(right_click_button).perform()    # Вызываем метод клика по правой клавише
#
# print('Произвели клик по правой клавише')
time.sleep(5)
new_date = driver.find_element(By.XPATH, "//input[@id='start.value']")
new_date.click()
new_date.send_keys(Keys.CONTROL + "a")
new_date.send_keys(Keys.BACKSPACE)
time.sleep(5)
new_date.send_keys("06.04.2021")
time.sleep(5)
new_date.send_keys(Keys.RETURN)
now_date = datetime.datetime.now().strftime("%d")
print(now_date)
date = int(now_date) + 1
# time.sleep(10)
# new_date = driver.find_element(By.XPATH, "//input[@id='start.value']")
# new_date.click()
# time.sleep(5)
# date_9 = driver.find_element(By.XPATH, "(//td[@class='day'])[9]")
# date_9.click()