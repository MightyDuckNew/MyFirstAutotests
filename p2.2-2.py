from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)
x1 = int(browser.find_element(By.ID, "input_value").text)
res = calc(x1)
print(res)
text_field = browser.find_element(By.ID, "answer").send_keys(res)
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
option2 = browser.find_element_by_css_selector("[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()
button = browser.find_element(By.XPATH, './/button[text()="Submit"]').click()
time.sleep(30)
browser.quit()
