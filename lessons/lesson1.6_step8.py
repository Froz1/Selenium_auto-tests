from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name('div.form-group:nth-child(1) input')
input1.send_keys("I")
input2 = browser.find_element_by_tag_name('div.form-group:nth-child(2) input')
input2.send_keys("P")
input3 = browser.find_element_by_tag_name("div.form-group:nth-child(3) input")
input3.send_keys("S")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
