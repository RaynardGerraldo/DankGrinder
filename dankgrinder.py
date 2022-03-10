#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys
import pickle
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://discord.com")

time.sleep(3)

def login_qr(driver):
    login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/header[2]/nav/div[2]/a')

    login_button.click()

    qr_scan = int(input("Scan qr, 1 for done 0 for cancel:  "))

    if qr_scan != 1:
        print("Not scanned")
        sys.exit()
    print("scanned")

    print(driver.current_url)

cmd_list = ["pls fish","pls dig","pls hunt"]
cmd_list2 = ["pls crime","pls search"]

@lru_cache
def send(driver,input_element): 
    for cmd in cmd_list:
        action = ActionChains(driver)
        action.move_to_element(input_element).send_keys(cmd).key_down(Keys.ENTER).perform()

    crime(driver,input_element)
    search(driver,input_element)
    time.sleep(35)
    send(driver,input_element)

def crime(driver,input_element):
    action = ActionChains(driver)
        
    wait_buttons = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME, "container-1v9gV9")))

    click_button = ["boredom","identity theft","fraud","murder","tax evasion","shoplifting","vandalism","drug distribution","cyber bullying","arson"]
          
    random.shuffle(click_button)
         
    time.sleep(0.8)
    action.move_to_element(input_element).send_keys("pls crime").key_down(Keys.ENTER).perform()
    for click in click_button:
        try:
           wait_button = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, f"//button[@class='component-1IAYeC button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN' and contains(.,'{click}')]")))

           elm = driver.find_element_by_xpath(f"//button[@class='component-1IAYeC button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN' and contains(.,'{click}')]")

           ActionChains(driver).move_to_element(elm).click().perform()
                
        except:
           print("Retry...")
           continue
        break

def search(driver,input_element):
    action = ActionChains(driver)
    action.move_to_element(input_element).send_keys("bot").key_down(Keys.ENTER).perform()
    
    wait_buttons = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME, "container-1v9gV9")))

    click_button = ["mailbox","pocket","bushes","vacuum","glovebox","grass","van","tree","fridge","area51","bus","bank","dog","shoe","washer","mels room","sewer","uber","dumpster","crawlspace","who asked","garage","air"]

    random.shuffle(click_button)

    time.sleep(0.8)
    action.move_to_element(input_element).send_keys("pls search").key_down(Keys.ENTER).perform()

    for click in click_button:
        try:
           wait_button = WebDriverWait(driver,1.2).until(EC.presence_of_element_located((By.XPATH, f"//button[@class='component-1IAYeC button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN' and contains(.,'{click}')]")))

           elm = driver.find_element_by_xpath(f"//button[@class='component-1IAYeC button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN' and contains(.,'{click}')]")

           ActionChains(driver).move_to_element(elm).click().perform()
                
        except:
            print("Retry....")
            continue
        break

login_qr(driver)

input_elm = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]/div")))

input_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]")

send(driver,input_element)
