from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_id('treasure')
input1_valuex = input1.get_attribute("valuex")
x = input1_valuex
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)
option1 = browser.find_element_by_id('robotCheckbox')
option1.click()
option2 = browser.find_element_by_id('robotsRule')
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

