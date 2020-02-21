import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser= webdriver.Firefox()
browser.get('https://www.google.com')
#elem = browser.find_element_by_css_selector('.gLFyf')
#elem.click()
#elems=browser.find_elements_by_css_selector('p')
#print(len(elems))

searchelem = browser.find_element_by_css_selector('.gLFyf')
searchelem.send_keys('navneetsingh')
searchelem.submit()
browser.back()


