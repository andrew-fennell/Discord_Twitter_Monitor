import asyncio
import discord
from discord.ext.commands import Bot
import scraper
import config


BOT_PREFIX = config.CONFIG['BOT_PREFIX']
TOKEN = config.CONFIG['TOKEN']
profile_url = config.CONFIG['PROFILE_URL']
channel_id = config.CONFIG['CHANNEL_ID']
interval = config.CONFIG['INTERVAL']

client = Bot(command_prefix=BOT_PREFIX)
channel = discord.Object(id=channel_id)


@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    print(client.user.id)
    print('----------')


async def tweet_monitor():
    prev = ''
    await client.wait_until_ready()
    while not client.is_closed:
        new = scraper.latest_tweet()
        if new != prev:
            await client.send_message(channel, new)
            prev = new
        await asyncio.sleep(interval)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        print('------------')
        await asyncio.sleep(600)


client.loop.create_task(tweet_monitor())
client.loop.create_task(list_servers())
client.run(TOKEN)

