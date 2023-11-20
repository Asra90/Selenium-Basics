from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://installonair.com/")

Wait = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.ID, 'file')))
driver.find_element(By.ID, 'file').send_keys(r"C:/Users/Asra Iqbal/Downloads/app-staging-release (1).apk")

Wait = WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.ID,'copy-target')))
link = driver.find_element(By.ID, 'copy-target').text

with open("E:\Automation Crash Course\AppUploadInstallOnAir\link.txt","w") as f:
   f.write(link)

print("successfully got link")















# full xpath and relative path difference is ID
# file opening in python
# loop 