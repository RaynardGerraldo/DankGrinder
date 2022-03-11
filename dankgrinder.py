#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://discord.com/login")
driver.maximize_window()
tries = int(sys.argv[1])
time.sleep(3)

def login_qr(driver):
    qr_scan = int(input("Scan qr and go to channel, 1 for done 0 for cancel:  "))

    if qr_scan != 1:
        print("Not scanned")
        sys.exit()
    print("scanned")

    print(driver.current_url)

def send(driver,input_element):
    cmd_list = ["pls fish","pls dig","pls hunt"]
    try:
        for cmd in cmd_list:
            print("fish dig hunt")
            input_element.send_keys(cmd[::-1])
            input_element.send_keys(Keys.ENTER)
    except Exception as e:
        print(getattr(e, 'message', repr(e)))       

def crime(driver,input_element):
    print("crime")
    input_element.click()
    time.sleep(0.8)

    input_element.send_keys("emirc slp")
    input_element.send_keys(Keys.ENTER)
    time.sleep(2)

    buttons_to_text = [elements.text for elements in driver.find_elements_by_class_name("children-2XdE_I")]
    buttons_to_text = buttons_to_text[-1].split("\n")
    random.shuffle(buttons_to_text)

    for click in buttons_to_text:
        try:
           wait_button = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, f"//button[@class='component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeSmall-wU2dO- grow-2sR_-F' and contains(.,'{click}')]")))

           elm = driver.find_element_by_xpath(f"//button[@class='component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeSmall-wU2dO- grow-2sR_-F' and contains(.,'{click}')]")

           if elm.is_enabled():
              elm.click()
        except Exception as e:
            print(getattr(e, 'message', repr(e)))
            continue
        break       

def search(driver,input_element):
    print("search")
    input_element.click() 
    time.sleep(0.8)

    input_element.send_keys("hcraes slp")
    input_element.send_keys(Keys.ENTER)
    time.sleep(1.5)

    buttons_to_text = [elements.text for elements in driver.find_elements_by_class_name("children-2XdE_I")]

    buttons_to_text = buttons_to_text[-1].split("\n")
    random.shuffle(buttons_to_text)

    for click in buttons_to_text:
        try:
           wait_button = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, f"//button[@class='component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeSmall-wU2dO- grow-2sR_-F' and contains(.,'{click}')]")))

           elm = driver.find_element_by_xpath(f"//button[@class='component-ifCTxY button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeSmall-wU2dO- grow-2sR_-F' and contains(.,'{click}')]")

           if elm.is_enabled():
              elm.click()
        except Exception as e:
            print(getattr(e, 'message', repr(e)))
            continue
        break

login_qr(driver)

input_elm = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]/div")))

input_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]")

for i in range(tries):
    send(driver,input_element)
    time.sleep(2)
    search(driver,input_element)
    time.sleep(2)
    crime(driver,input_element)
   	
    print("Cooldown....")
    time.sleep(35)
