from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)
x1 = int(browser.find_element(By.ID, "num1").text)
x2 = int(browser.find_element(By.ID, "num2").text)
res = str(x1 + x2)
print(type(res))
dropdown = Select(browser.find_element(By.ID, "dropdown"))
dropdown.select_by_value(res)
button = browser.find_element(By.XPATH, './/button[text()="Submit"]').click()
time.sleep(30)
browser.quit()
