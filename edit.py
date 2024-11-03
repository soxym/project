import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.maximize_window()



iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)    # переключение на iframe

pole = driver.find_element(By.XPATH, "//div[@id="__next"]/div/div[2]")    # обращаемся к текстовому полю

time.sleep(3)

pole.send_keys(Keys.CONTROL + "a")    # выделяем содержимое поля

# 1. удаляем выделенный текст

pole.send_keys(Keys.DELETE)

# 2. получаем содержимое (значение) поля

value_pole = pole.text

# 3. производим редактирование текста

click_editing_panel_bolt = driver.find_element(By.XPATH, "//button[@title='Bold']")    # обращаемся к кнопке редактирования Bolt

click_editing_panel_bolt.click()

