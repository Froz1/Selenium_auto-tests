from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name('div.form-group:nth-child(1) input')
input1.send_keys("I")
input2 = browser.find_element_by_name('last_name')
input2.send_keys("P")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("S")
input4 = browser.find_element_by_id("country")
input4.send_keys("R")
button = browser.find_element_by_css_selector("button.btn")
button.click()
