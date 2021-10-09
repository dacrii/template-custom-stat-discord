import discord, asyncio
from discord import PartialEmoji
from discord.ext import tasks, commands

client = commands.Bot(command_prefix='>>', self_bot=True)

@client.event
async def on_connect():
#	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="my gf", details="In My Dream", state="She's so beautiful"))
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name="%"))
	await client.change_presence( activity=discord.CustomActivity(name='Handling My Business!', emoji='<a:Tail_Wag:711971800157913088>'))
	print("connected.")

# @client.command()
# async def test(ctx):
# 	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="my gf", details="In My Dream", state="She's so beautiful"))
# 	print("x")

client.run("fill me up baby", bot=False)