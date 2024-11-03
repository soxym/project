import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.maximize_window()
#взаимодействие с сообщение в котором только ок
# button_login = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
# button_login.click()
# print('click button')
# time.sleep(3)
# driver.switch_to.alert.accept()
#взаимодействие с сообщение в котором ок и отмена
button_login = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
button_login.click()
print('click button')
time.sleep(3)
# driver.switch_to.alert.accept() #подтверждение
driver.switch_to.alert.dismiss() #отклонение