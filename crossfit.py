#!/usr/bin/env python3

# NOTE: Run with 'crossfit.py | tee output_file.txt'
# To use this personally, change hard code of variables:
# browser (the location saved)
# user_name
# start, end  (the dates being scoured)

import os
import sys
import time
import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

browser = webdriver.Chrome('/home/tclack/bin/chromedriver')
# YMMV this is the chromedriver I use and the location
urlstart = "https://www.crossfit.com/workout/"
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
  
    print(':::::',current.strftime('%Y%b%d'),':::::')
    write_date = '::::: '+current.strftime('%Y%b%d')+' :::::'
    #os.system("echo -e "+write_date+" >> "+output_file)

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
            print(line)
            write_WOD = line
            #os.system("echo -e "+write_WOD+" >> "+output_file)


    print("\n")

    #### My Post ####

    users = soup.find_all("div",{"class":"name"})
    posts = soup.find_all("div",{"class":"text"})
    index = 0
    user_name = "clack_attack"
    for user in users:
        if user_name in user.text.lower(): 
            print(user.text)
            # My username changes and I don't always capitalize
            # Strong assumption: 
            # there are as many <div class=name> tags as <div class = text>
            # This seems to be the case so my text matches up... perhaps this should
            # be made more general/exact
            print(posts[index].text)
            write_post = posts[index].text
            #os.system("echo -e "+write_post+"\n\n\n\n\n >> "+output_file)
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
        #print('nahbro')
        print()
    sys.stdout.flush()
    # flush allows displaying stdout to terminal AND writing to the output file
    # otherwise we'd have to wait until the script finishes to see the output file
    # It's psychologically nicer when we see an actual output

#output_file = str(datetime.datetime.now().strftime('%d%b%Y-%H:%m:%S'))+".txt"
#os.system("touch "+output_file)
# want to make the file from python to generate new file each time
# consider the above a work in progress then
begin = datetime.date(2009,3,1)
end = datetime.date(2009,3,31)
# these dates may be changed at a whim
current = begin
for i in range((end-begin).days):
    current += datetime.timedelta(days=1)
    urlmiddle = current.strftime('%Y/%m/%d')
    url = urlstart+urlmiddle+urlend
    Collect()




browser.close()
browser.quit()
