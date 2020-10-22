import asyncio
import time
import discord
from discord.ext.commands import Bot

import web_scrape
import config


BOT_PREFIX = config.CONFIG['BOT_PREFIX']
TOKEN = config.CONFIG['TOKEN']
profile_url = config.CONFIG['PROFILE_URL']
#channel_id = config.CONFIG['CHANNEL_ID']
interval = config.CONFIG['INTERVAL']

prev_tweet = ''

client = Bot(command_prefix=BOT_PREFIX)
#channel = client.get_guild()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Twitter"))
    client.loop.create_task(list_servers())

def tweet_monitor(profile):
    global prev_tweet
    if profile == "":
        profile = profile_url
    
    new = web_scrape.latest_tweet(profile)
    if new != prev_tweet:
        prev_tweet = new
        print("New tweet found: " + new)
        print()
        return new
    else:
        return -1


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed():
        print()
        print('------------')
        print("Current servers:")
        for guild in client.guilds:
            print(guild.name)
        print('------------')
        print()
        await asyncio.sleep(600)

@client.command(name='server')
async def fetchServerInfo(context):
	guild = context.guild
	
	await context.send(f'Server Name: {guild.name}')
	await context.send(f'Server Size: {len(guild.members)}')

@client.command(name='scrape')
async def callTwitterScrape(context, profile=profile_url):
    profile = str(profile)
    while True:
        latest = tweet_monitor(profile)
        if latest == -1:
            print("No new tweets.\n")
        else:
            await context.send(str(latest))
        
        time.sleep(interval)

#client.loop.create_task(tweet_monitor())    
#client.loop.create_task(list_servers())
client.run(TOKEN)
