from selenium import webdriver
import os 


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name('firstname')
input1.send_keys("I")
input2 = browser.find_element_by_name('lastname')
input2.send_keys("P")
input3 = browser.find_element_by_name("email")
input3.send_keys("S")

i = browser.find_element_by_id('file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'lesson2.2_step8.txt')            
i.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()
