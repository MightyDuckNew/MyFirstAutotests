from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
filepath = os.path.join(current_dir, 'test.txt')
in1 = browser.find_element(By.NAME, "firstname").send_keys('testname')
in2 = browser.find_element(By.NAME, "lastname").send_keys('testlastname')
in3 = browser.find_element(By.NAME, "email").send_keys('testemail')
browser.find_element(By.NAME, "file").send_keys(filepath)
attach = browser.find_element(By.NAME, "firstname").send_keys('testname')
button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(30)
browser.quit()
