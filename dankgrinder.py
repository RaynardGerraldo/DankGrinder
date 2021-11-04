#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import sys
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


name = input("Name: ")
filename = name + ".pkl"

driver = webdriver.Firefox()
driver.get("http://discord.com")

time.sleep(3)
login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/header[2]/nav/div[2]/a')

login_button.click()

qr_scan = int(input("Scan qr, 1 for done 0 for cancel:  "))

if qr_scan != 1:
   print("Not scanned")
   sys.exit()
print("scanned")

print(driver.current_url)

cmd_list = ["pls fish","pls dig","pls hunt"]

def send(driver,input_element): 
    for cmd in cmd_list:
        action = ActionChains(driver)
        action.move_to_element(input_element).send_keys(cmd).key_down(Keys.ENTER).perform()
    
    time.sleep(40)
    send(driver,input_element)

input_elm = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]/div")))

input_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]")
send(driver,input_element)
