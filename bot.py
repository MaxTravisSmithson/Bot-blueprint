import discord
import config

from discord.ext import commands

bot = commands.Bot(command_prefix=config.PREFIX, intents=discord.Intents.all()) # You will need to research intents and enable them in your developer dashboard as a lot of tutorials leave them out as they are fairly new

# EVENTS

# This event detects when the bot is loaded up and will just send a message in the console to confirm
@bot.event
async def on_ready():
    print("--------------")
    print("Bot is online!")
    print("--------------")

# This event will detect a player joining and send a message to them with whatever you put in the speech marks ""
# The function on_member_join takes the input member and we use that to know who to send our message to
@bot.event
async def on_member_join(member):
    await member.send("Welcome to our server! We hope you enjoy your time here. Type '!help' to see a list of my commands!") # !help is a build in function of dicord.py and displays a list of the commands you can categorise and what the commands do

# Commands

# COMMANDS

# This is a simple single output command where the player types a command and get a reply
# The function we define after def is the name of the command so the player would type '!hello' to use it
# Taking the ctx in means that when we do .send it will go to whatever server channel the message was typed in or even into DM's with the bot if we use it there
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! \nHope you have a good day!") # \n means the text after is printed on a new line

# This command will show the latency for the bot
# The ** ** are there to make the part inbetween bold
@bot.command()
async def ping(ctx):
    await ctx.send(f"I have a latency of **{round(bot.latency * 1000, 1)}** ms") # Round is a built in python function to round the number and bot.latency is part of discord.py to get the bot latency of course

bot.run(config.TOKEN) # This is what actually tells our program to run the bot with the associated token from the config file and also needs to be after all the commands