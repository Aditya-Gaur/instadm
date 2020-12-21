from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

def instadm():
    user = "piyush_agarwal_official"
    password = "agarwal1"
    rec = input("Enter Username\n")
    msg = input("Enter Your Message\n") 
    time.sleep(5)

    #Loginning In

    driver = webdriver.Chrome("D:\chromedriver.exe")
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    user_name = driver.find_element_by_name("username")
    user_name.send_keys(user)
    pass_word=driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password")
    driver.find_element_by_name("password").send_keys(Keys.ENTER)
    time.sleep(3)

    #Messaging

    driver.get("https://www.instagram.com/"+rec)
    driver.find_element_by_class_name("_8A5w5").click()
    time.sleep(3)
    driver.find_element_by_class_name("HoLwm ").click()
    time.sleep(1)
    driver.find_element_by_class_name("ItkAi").click()
    time.sleep(1)
    pyautogui.write(msg)
    time.sleep(1)
    pyautogui.press('enter')
