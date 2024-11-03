# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # # # options = webdriver.ChromeOptions
# # # # options.add_experimental_option('detach', True)
# # # # driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmSelenium\\pythonProject', options=options)
# #
# driver = webdriver.Firefox(executable_path='C:\\Users\\User\\PycharmSelenium\\pythonProject\\geckodriver.exe')
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# # user_name = driver.find_element_by_id("user-name")
# user_name = driver.find_element(By.ID,"user-name")
# user_name.send_keys("standard_user")

# time.sleep(10)
# driver.close()

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# options = webdriver.FirefoxOptions()
# options.add_argument("--ignore-certificate-errors")
# options.binary_location = 'D:\\stepik\\geckodriver.exe'
# driver = webdriver.Firefox(options=options)
#
# base_url = 'https://www.saucedemo.com/'
# driver.get(base_url)
# driver.maximize_window()

# time.sleep(5)
# driver.close()


# from selenium import webdriver
#
# # browser = webdriver.Chrome()
# browser = webdriver.Firefox()
#
#
# def main():
#     browser.maximize_window()
#     browser.get('https://www.saucedemo.com')
#     time.sleep(10)
#     browser.close()
#
#
# if __name__ == '__main__':
#     main()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# user_name = driver.find_element_by_id("user-name")
user_name = driver.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")