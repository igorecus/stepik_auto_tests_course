from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

btn1 = browser.find_element(By.ID, 'book')
browser.execute_script("return arguments[0].scrollIntoView(true);", btn1)
btn1.click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)

button = browser.find_element(By.ID, 'solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)

browser.quit()