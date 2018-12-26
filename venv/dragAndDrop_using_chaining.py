from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://jqueryui.com/droppable/")

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

try:
    actions = ActionChains(driver)
    source_position = driver.find_element_by_xpath("//body/div[1]")
    target_position = driver.find_element_by_xpath("//body/div[2]")
    actions.click_and_hold(source_position).move_to_element(target_position).release().perform()
except:
    print("Operation failed")


