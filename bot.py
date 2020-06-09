import os
import logging
import traceback

from discord.ext import commands
from utils.google_search import GoogleSearch
from dotenv import load_dotenv
from utils.helper import prettify_search
from utils.database_client import DatabaseClient

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

# Bot User Object
bot = commands.Bot(command_prefix='!')
print('Connecting Bot to Server...')

# Clients to perform Search and Database operations
search_client = GoogleSearch()
database_client = DatabaseClient()


@bot.event
async def on_ready():
    """This event gets called when Bot gets connected to Server"""
    print(f'{bot.user.name} is connected to the Server')


@bot.event
async def on_member_join(member):
    """This event gets called when someone join the server"""
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.event
async def on_message(message):
    """This event gets called when someone messages in the chat area to which our Bot is connected"""

    # Important! Our Bot cannot differentiate between Bot and Normal user. So in order to handle the recursive call
    # That may happen when The bot user send message in the channel, This check is being used
    if message.author == bot.user:
        return
    content = message.content.lower()

    # Send simple Greeting when someone say Hi, Hey in the Channel
    if content.startswith('hi') or content.startswith('hey'):
        await message.channel.send(f'Hey, {message.author.name}!')

    # Process the Discord commands
    await bot.process_commands(message)


@bot.command(name='google', help='Do Google search. eg. !google I Love Python!')
async def _search(ctx, *args):
    """This event is called when someone use !google command in the Discord channel"""

    # Make query string for Google search
    query = ' '.join(args)

    # Perform Google search
    search = search_client.search(query=query)

    # Prettify the search response
    response = prettify_search(search)

    # Send the search response in Discord
    await ctx.send(response)

    # Insert the search keyword to the database
    await database_client.push_history(query, ctx.author.id)


@bot.command(name='recent', help='Check Google search history. eg. !recent Python')
async def _history(ctx, *args):
    """This event is called when someone use !recent command in the Discord channel"""
    # Make query string
    query = ' '.join(args)

    # Perform database request for Author search history
    result = database_client.author_history(query, ctx.author.id)
    await ctx.send(result)


@bot.event
async def on_command_error(ctx, error):
    """This event gets called when illegal command is being used"""
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send(error)


@bot.event
async def on_error(event, *args, **kwargs):
    """This event gets called when some error occurs"""
    trace = traceback.format_exc()
    if event == 'on_message':
        logging.error(f'Unhandled message: {args[0]}\n', extra=trace)
    else:
        logging.error(f'Something went wrong', extra=trace)
        raise

bot.run(TOKEN)
