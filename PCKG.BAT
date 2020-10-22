:End
pyinstaller --onefile --hidden-import=asyncio,time,discord,discord.ext.commmands,webdriver_manager.chrome discord_bot.py web_scrape.py