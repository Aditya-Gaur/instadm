import pyttsx3
import datetime
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
rate=engine.getProperty("rate")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",125)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour<=12:
        speak("Good Morning")

    else:
        speak("Good Afternoon")

    print("how may i help u")
    speak("how may i help u")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

def op():
    webbrowser.open("https://google.com")

takecommand()
try:
    print("Recognizing...")
    query = r.recognize_google(audio)
    print("User said "+query)
except:
    pass
