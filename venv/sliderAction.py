from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://jqueryui.com/slider/")

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

try:
    actions = ActionChains(driver)
    slider_button = driver.find_element_by_xpath("//div[@id='slider']/span")
    actions.drag_and_drop_by_offset(slider_button,100,0).perform()
except:
    print("operation failed")
