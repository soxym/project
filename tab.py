import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = 'https://testpages.eviltester.com/styled/windows-test.html'
driver.get(base_url)
driver.maximize_window()


#переключение между вкладками

# button_login = driver.find_element(By.XPATH, "//a[@id='gobasicajax']")
# button_login.click()
# print('click button')
# print(driver.current_url)
#
# driver.switch_to.window(driver.window_handles[1])
# print(driver.current_url)
# time.sleep(3)
#
# driver.switch_to.window(driver.window_handles[0])
# print(driver.current_url)

#переключение между окнами
# button_login = driver.find_element(By.XPATH, "//a[@id='gobasicajax']")
# button_login.click()
# print('click button')
# print(driver.current_url)