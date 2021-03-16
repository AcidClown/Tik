#coding: utf-8

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Style
import os, sys, time, traceback, pickle, random, colorama

def getdeveloper():
    dev = "TΞILΛW#0001"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/qa1ftnHs")).read().decode()
    except:
        pass
    return dev

def clear():
    
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    os.system("mode con: cols=105 lines=30")
    

def logo():
    developer = getdeveloper()
    try:
        text = """                                   
                         ▄▄▄▄▄▄▪  ▄ •▄▄▄▄▄▄▄      ▄ •▄    ▄▄▄▄·      ▄▄▄▄▄▄      
                          •██  ██ █▌▄▌▪•██  ▪     █▌▄▌▪   ▐█ ▀█▪▪     •██        
                           ▐█.▪▐█·▐▀▀▄· ▐█.▪ ▄█▀▄ ▐▀▀▄·   ▐█▀▀█▄ ▄█▀▄  ▐█.▪     
                           ▐█▌·▐█▌▐█.█▌ ▐█▌·▐█▌.▐▌▐█.█▌   ██▄▪▐█▐█▌.▐▌ ▐█▌· 
                           ▄██ ▄██·█  █ ▄██  ▀█▄▀▪·█ ▀█▄  ·▀███▀ ▀█▄▀▪ ▄██  \n                    
        """
        bad_colors = ['LIGHTRED_EX', 'RED']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.RESET + "\t\t\t          Follow Me on Youtube: Dr. Teilaw\n")

    except KeyboardInterrupt:
        sys.exit()

clear()
logo()

maxi = 0
developer = getdeveloper()
boosted_username = input('{}\n[>] {}TikTok Username: {}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
print('  ')
options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,900')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
browser.minimize_window()
wait = WebDriverWait(browser, 3)

from selenium import webdriver

init()
os.system('title ' + ' TikTok Booster made by '+ developer + ' - Boost: @{}'.format(boosted_username))

def countdown():
    while True:
        time.sleep(10)
        try:
            browser.find_element_by_xpath('//*[@id="show_tkfollow"]/div/div/div/form/div/div/button').click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/form/button')))
            break
        except:
            continue
            pass
def run():
    global username
    developer = getdeveloper()
    try:
        browser.find_element_by_xpath('//*[@id="show_tkfollow"]/div/div/div/form/div/div/button').click() #Search link
        try:
            followers = browser.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/form/div[4]/span').text #Show followers
            time.sleep(1)
        except:
            pass
        time.sleep(5)
        while True:
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/form/button')))
                break
            except:
                run()
        browser.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/form/button').click() #Send followers
        print('  ')
        print('{}[>] {}Followers Sent{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
        os.system('title ' + ' TikTok Booster by '+ developer + ' ~ Boost: @{} - Followers: {}'.format(username, followers))
        time.sleep(5)
        countdown()
        run()
    except:
        run()

def paste_link():
    global boosted_username
    try:
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="show_tkfollow"]/div/div/div/form/div/input').send_keys(boosted_username) #Link where is paste
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="show_tkfollow"]/div/div/div/form/div/div/button'))) #Search link
        print('  ')
        print("{}[>] {}Pasted Username...{}".format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
        run()
    except Exception as e: 
        print(e)

def maximize():
    global maxi
    maxi += 1
    if maxi == 1:
        print('  ')
        print('{}[>] {}Please do the Captcha to continue.{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
        browser.maximize_window()
    elif maxi >= 1:
        pass
    else:
        pass

def start():
    try:
        browser.get("https://vipto.de/")
        time.sleep(2)
        while True:
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/h2/span')))
                print('  ')
                print('{}\n[X] {}Please Disable Adblock.{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
                continue
            except:
                pass
                break
        while True:
            try:
                maximize()
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/form/div/input[1]')))
                continue
            except:
                pass
                browser.minimize_window()
                break
    except:
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/ul/li/a')))
            print('  ')
            print("{}[>] {}The Page didn't load.{}".format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
            input()
        except:
            pass
    print('  ')
    print('{}[>] {}Captcha OK.{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
    time.sleep(1)
    try:
        browser.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/button').click()
        time.sleep(1)
    except:
        print('  ')
        print("{}[>] {}Error, Cannot find Element{}".format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
        pass
    clear()
    logo()
    print('{}[>] {}Starting...{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
    paste_link()

start()
