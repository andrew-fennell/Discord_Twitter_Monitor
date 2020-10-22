import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import config

BOT_PREFIX = config.CONFIG['BOT_PREFIX']
TOKEN = config.CONFIG['TOKEN']
interval = config.CONFIG['INTERVAL']
twitter_user = config.CONFIG['TWITTER_USER']
twitter_pass = config.CONFIG['TWITTER_PASS']

def twitter_login(s):
    print("Logging in...")
    s.get("https://twitter.com/login")
    time.sleep(2)
    user_box = s.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
    pass_box = s.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

    user_box.send_keys("twitter_user")
    pass_box.send_keys("twitter_pass$")

    btn = s.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
    btn.click()

    if (s.current_url == 'https://twitter.com/home'):
        print("Successfully logged in.")
    else:
        print("Login failed.")
    print()

def latest_tweet(profile_url):

    base = "https://twitter.com/"
    if (not base in profile_url):
        url = base + profile_url
    else:
        url = profile_url
    
    print("Scanning: " + url)

    s.get(url)
    time.sleep(5)

    # is there a pinned tweet?
    pinned_tweet = False
    try:
        s.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/span')
        pinned_tweet = True
    except:
        pinned_tweet = False

    # actual text of tweet
    if (not pinned_tweet):
        tweet = s.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]')
    else:
        tweet = s.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/article/div/div/div/div[2]')

    # link to tweet
    tweet_link = s.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a')
    link = tweet_link.get_attribute('href')


    return str(tweet_link.get_attribute('href'))


CHROME = ChromeDriverManager().install()


print()
print()
print("=======================================================")
print()
print()

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
s = webdriver.Chrome(CHROME, options=chrome_options)

if (twitter_user != "" and twitter_pass != ""):
    twitter_login(s)



