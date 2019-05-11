#!/usr/bin/env python3
import time
import selenium
from selenium import webdriver
from multiprocessing import Process
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
#driver = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome(executable_path='/home/tclack/bin/chromedriver',chrome_options=chrome_options)
urlstart = "https://www.crossfit.com/workout/2009/03/"
urlend = "#/comments"

"""
for i in range(1,31):
    urlmiddle = str(i)
    if len(urlmiddle) == 1:
        urlmiddle = "0"+urlmiddle
    url = urlstart+urlmiddle+urlend
    p = Process(target=Collect)
    p.start()
    p.join()
"""
def Collect():
    browser.get(url)


    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

    string = "Clack_Attack"
    time.sleep(5)
    if string in innerHTML:
        print('Trevor present in',url)
    else:
        print('nahbro')


for i in range(1,31):
    urlmiddle = str(i).zfill(2)
    url = urlstart+urlmiddle+urlend
    Collect()
    #p = Process(target=Collect, args=())
    #p.start()
    #p.join()


browser.close()
browser.quit()
