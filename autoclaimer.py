from os import system
import requests , uuid , time 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time
from colorama import Fore, Back, Style
import sys


#tiktok detection bypass
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options) #driver path

driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.set_window_size(1260, 720) #chrome size feel free to adjust

#checking if your python isn´t 2
if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)

req = requests.session()
uid = uuid.uuid4()
system("title " + "t.me/undecryptable")
time.sleep(2)
os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')
print('')
print(Fore.CYAN + '          TikTok AutoClaimer by yin/who?')
user = input(Back.BLACK + Fore.WHITE + "Enter @")
os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')
time.sleep(2)
#driver.get("https://www.tiktok.com/signup/create-username")
#time.sleep(1)
#driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(user)
#driver.find_element_by_xpath("//button[@class='login-button-31D24 disable-fEJEn highlight-1TvcX']").click()
driver.get("https://tiktok.com")
#driver.get("https://www.tiktok.com/login/")
print(Fore.CYAN + '          Login Into TikTok!') 
print('')
print('')
check = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.LIGHTMAGENTA_EX +"yin" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" ")#input "True" to start checker

#Auto Claimer by yin/timer/https://github.com/r6f


while check: #checker checking for username
    url1 = f'https://www.tiktok.com/@{user}?'
    hed = {     
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max - age = 0',
        'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25'}
    st = req.get(url1,headers=hed)
    if st.status_code == 404:
        print(Back.BLACK + Fore.GREEN + f'\n@{user} is available')#if is username available it will get to change username site and change it
        driver.get("https://www.tiktok.com/signup/create-username")
        time.sleep(0.3)
        driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(user)
        time.sleep(2.1)
        driver.find_element_by_xpath("//button[@class='login-button-31D24 highlight-1TvcX'][@type='submit']").click()
        time.sleep(2)
    elif st.status_code == 200:
        print(Back.BLACK + Fore.MAGENTA + '['+ Fore.WHITE + '-' + Fore.MAGENTA + ']' + Fore.MAGENTA + ' Swapping ' + Back.BLACK + Fore.WHITE + f'@{user}...')	
    else:
        print(Back.BLACK + Fore.RED + 'IP BLOCKED!')
