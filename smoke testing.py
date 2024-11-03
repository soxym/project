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

'''Info product 1'''
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select_product_1")

cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print("enter cart")

"""info cart product_1"""
cart_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("info cart product_1 good")
cart_price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("info cart price product_1 good")

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("click checkout")

"""Select User info"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Max")
print("input first_name")

Last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
Last_name.send_keys("Sen")
print("input last_name")

Zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
Zip.send_keys("1234")
print("input Zip")


Continue = driver.find_element(By.XPATH, "//input[@id='continue']")
Continue.click()
print("click Continue")

"""info finish product_1"""
finish_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("info finish product_1 good")
finish_price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("info finish price product_1 good")

summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: " + value_finish_price_product_1

assert value_summary_price == item_total
print("total summary price good")

