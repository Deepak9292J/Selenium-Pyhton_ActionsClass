from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://learn.letskodeit.com/p/practice")

driver.execute_script("window.scrollBy(0,775) ;")
time.sleep(3)
try:
    actions = ActionChains(driver)
    element_to_be_hovered = driver.find_element_by_xpath("//button[@id='mousehover']")
    element_to_be_clicked = driver.find_element_by_xpath("//a[contains(text(),'Reload')]")
    actions.move_to_element(element_to_be_hovered).move_to_element(element_to_be_clicked).click().perform()
except:
    print("Hover failed!")
