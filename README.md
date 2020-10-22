# Discord_Twitter_Monitor

Discord Twitter Monitor, Python discord bot

# Usage

Monitors a single Twitter profile and when they update their status, it sends a message in a specific Discord channel with the link to the new tweet.

This monitor bot is VERY basic in its abilities. If you have suggestions for features for the bot in later versions, please let me know!

# Setup

The config file will ask for a few things before the bot will function.
Here is how to create a server, application, and bot:

1. Create a server
If you don't already have a server, create one free one at https://discordapp.com. Simply log in, and then click the plus sign on the left side of the main window to create a new server.

2. Create an app
Go to https://discordapp.com/developers/applications/me and create a new app. On your app detail page, save the Client ID. You will need    it later to authorize your bot for your server.

3. Create a bot account for your app
4. After creating app, on the app details page, scroll down to the section named bot, and create a bot user. Save the token, you will need it later to run the bot.

4. Authorize the bot for your server
Visit the URL https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot but replace XXXX with your app client ID. Choose the server you want to add it to and select authorize. 
Paste the client id into the config file.

5. Copy and Paste your bot's TOKEN into the config file.
This can be found in applications, then bot.

6. Customize the interval that the bot will scan twitter (interval in seconds)

7. Customize your bot's command prefixes.

8. AFTER YOU COMPLETE THE CONFIG, Run PCKG.BAT.

9. You can run the .exe file located in the /dist folder to start the bot. 
Keep it running while you want your bot to be online.

# Commands

Type !scrape <profile> in the channel you want the bot to send new posts to. 

Example: If you want to scrape https://twitter.com/ElonMusk
		 You need to type !scrape ElonMusk
