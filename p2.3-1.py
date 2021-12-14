from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
alert = browser.switch_to_alert().accept()
x1 = int(browser.find_element(By.ID, "input_value").text)
res = calc(x1)
answer = browser.find_element(By.ID, "answer").send_keys(res)
browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(30)
browser.quit()
