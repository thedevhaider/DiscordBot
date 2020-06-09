# DiscordBot
A simple DiscordBot. You can create the Bot User on Discord Developers and give its Client ID to this Bot. I will help you out how you can set this Bot up for you. But first lets talk about which technologies i have used to build this. 

Technologies: Python 3.7, MongoDB, Custom Google Search Engine and Heroku

The code is written in Python language. I have used Google Search API to perform Search operation using !google [keywords...] command through Discord. You can also see your recent searches using !recent [keywords..] command. MongoDB is for persisting the User's search history and I have deployed this Bot on Heroku!

If you are excited as I am then let's jump into setting up the project:-

1. First install Python 3.XX.
2. Install everything from the requirements.txt using pip install -r requirements.txt
3. Make an .env file in the project root directory and add the following keys in it: DISCORD_TOKEN, API_KEY, CSE_KEY, MONGODB_CONNECTION
4. You will get the DISCORD_TOKEN after creating your Bot User on Discord Developers portal. After creating the Bot user integrate it with any Guild. Refer to this for creating Discord Bot User https://discord.com/developers/applications
5. You need to have the Google Project API key in order to perform Google Search. You can have it by Creating Google project on Google Console. Refer this https://console.developers.google.com/cloud-resource-manager
6. You need Custom Search Engine key as well for performing search operation. You can have it by creating the the CSE app on the Google console. Refer this https://developers.google.com/custom-search/docs/tutorial/creatingcse
7. You need the MongoDB connection string for Persisting History. You can refer to https://mlab.com/ which i have used
8. Run the Bot from the bot.py file using python bot.py

BOOM!!

