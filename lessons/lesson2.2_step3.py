from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_id('num1')
input2 = browser.find_element_by_id('num2')
num1 = input1.text
num2 = input2.text
num = int(num1) + int(num2)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_visible_text(str(num)) # ищем элемент с текстом "Python"

button = browser.find_element_by_css_selector("button.btn")
button.click()

