# 1)использовать явное ожидание, с ним Мы познакомимся в следующем уроке
#
# 2)обработать данное исключение.


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))



from selenium.common.exceptions import NoSuchElementException #импортируем нужное исключение



try:
    element = driver.find_element(By.XPATH, "my_element") # осуществляем поиск элемента
    element.click()
except NoSuchElementException: # указываем ожидаемое исключение
    print("Элемент не найден")
# Мы отловили данную ошибку и получили об этом сообщение, но данный подход не поможет в наших тестах, так как кнопка не
# нажата и тест не может быть продолжен. Поэтому Мы должны доработать наш тест. Как это можно сделать, например:

from selenium.common.exceptions import NoSuchElementException #импортируем нужное исключение


try:
    element = driver.find_element(By.XPATH, "my_element") # осуществляем поиск элемента
    element.click()
except NoSuchElementException: # указываем ожидаемое исключение
    print("Получили NoSuchElementException")
    time.sleep(5)
    driver.refresh() # бновление страницы
    time.sleep(5)
    element = driver.find_element(By.XPATH, "my_element")
    element.click()