'''
Created on Jan 23, 2020

@author: Dattatray.Jadhav
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome("D:\Python\SeleniumWithPython\SeleniumWithPythonPractice\driver\chromedriver.exe")
#driver=webdriver.Firefox
#driver=webdriver.Ie
#driver=webdriver.Safari
#driver=webdriver.Edge

driver.set_page_load_timeout(5)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")

#Explicit wait
#element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME), "Submit"))
driver.find_element_by_name("Submit").click()
print(driver.title)
driver.get_screenshot_as_file("D:\\Python\\a.png")  #single slash beth path was not working
driver.quit()

