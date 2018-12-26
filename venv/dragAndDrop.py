from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://jqueryui.com/droppable/")
try:
    actions = ActionChains(driver)
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
    source_position = driver.find_element_by_xpath("//body/div[1]")
    target_position = driver.find_element_by_xpath("//body/div[2]")
    actions.drag_and_drop(source_position,target_position).perform()
except:
    print("Operation failed")


