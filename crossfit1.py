#!/usr/bin/env python3
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Process
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

monthDict={'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun', '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}


browser = webdriver.Chrome('/home/tclack/bin/chromedriver')
urlstart = "https://www.crossfit.com/workout/2009/03/"
urlend = "#/comments"


def waitForLoad(browser):
    try:
        WebDriverWait(browser, 10, ignored_exceptions=[
            NoSuchElementException, TimeoutException
        ]).until(EC.presence_of_element_located((By.CLASS_NAME,'name')))
    except TimeoutException:
        print("Error, timed out, trying again")
        browser.refresh()
        waitForLoad(browser)
        return


def Parse(innerHTML):

    soup = BeautifulSoup(innerHTML,"html.parser")

    #### Get Date #####
    date = soup.find("h1").text
    date = date.split(' ')
    datestring = '20'+date[1]
    year = datestring[0:4]
    month = datestring[4:6]
    month = monthDict[month]
    day = datestring[6:]
    print(':::::',day,month,year,':::::')

    ##### Get WOD description #####
    WOD = soup.find("div",{"class":'content'})
    WODdescription = WOD.find_all('p')
    for i in range(len(WODdescription)):
        line = WODdescription[i].text
        if line.split(' ')[0]=='Post':
            break
        # first few elements are title and description, often there is addition info
        # each WOD is always like: 'Post time to comments', so I don't want that or
        # any of the links or junk that follows"
        else:
            print(WODdescription[i].text)
    print("\n")

    #### My Post ####

    users = soup.find_all("div",{"class":"name"})
    posts = soup.find_all("div",{"class":"text"})
    index = 0
    for user in users:
        if "clack_attack" in user.text.lower(): 
            print(user.text)
            # My username changes and I don't always capitalize
            print(posts[index].text)
        index += 1
    print('\n'*5)


def Collect():
    browser.get(url)
    #wait = WebDriverWait(browser,10)
    #wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'name')))
    waitForLoad(browser)

    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
    user = "Clack_Attack"
    if user in innerHTML:
        #print('user present in',url)
        Parse(innerHTML)
    else:
        print('nahbro')




for i in range(1,31):
    urlmiddle = str(i).zfill(2)
    url = urlstart+urlmiddle+urlend
    Collect()




browser.close()
browser.quit()
