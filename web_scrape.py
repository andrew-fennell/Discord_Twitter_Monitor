import requests
from bs4 import BeautifulSoup
import config


BOT_PREFIX = config.CONFIG['BOT_PREFIX']
TOKEN = config.CONFIG['TOKEN']
profile_url = config.CONFIG['PROFILE_URL']
channel_id = config.CONFIG['CHANNEL_ID']
interval = config.CONFIG['INTERVAL']


def latest_tweet(given_url):
    url = profile_url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find(class_="ProfileTimeline")
    div_list = div.find_all('li')

    boop = ''
    for x in div_list:
        boop += str(x)

    split = boop.split('</div>')

    tweet_list = []
    temp = []
    for x in split:
        if 'original-tweet' in x and 'data-permalink-path' in x:
            temp.append(x)

    temp2 = []
    for x in temp:
        splitter = x.split(' ')
        temp2.append(splitter)

    for x in temp2:
        for y in x:
            if 'data-permalink-path' in y:
                final = y.split('=')
                tweet_list.append(final)

    tweet_links = []

    for tweet in tweet_list:
        tweet.remove('data-permalink-path')
        refined_link = tweet[0].replace('"', '')
        tweet_links.append(refined_link)

    link = 'https://twitter.com'
    if len(tweet_links) < 1:
        return 'No tweets on this profile.'
    elif len(tweet_links) == 1:
        return link + tweet_links[0]
    else:
        return link + tweet_links[1]


print(latest_tweet(''))

