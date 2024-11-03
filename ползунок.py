import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()
# actions = ActionChains(driver)
# price = driver.find_element(By.XPATH, "//input[@id='id2']")
# actions.click_and_hold(price).move_by_offset(20, 0).release().perform()
# print('price +')