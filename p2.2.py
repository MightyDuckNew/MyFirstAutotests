from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)
x_el = browser.find_element(By.ID, "treasure")
treasured_x = x_el.get_attribute("valuex")
print(treasured_x)
result = calc(treasured_x)
print(result)
text_field = browser.find_element(By.ID, "answer")
text_field.send_keys(result)
option1 = browser.find_element(By.ID, "robotCheckbox").click()
option2 = browser.find_element(By.ID, "robotsRule").click()
button = browser.find_element(By.XPATH, './/button[text()="Submit"]').click()
time.sleep(30)
browser.quit()
