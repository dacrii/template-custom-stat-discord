import discord, asyncio
from discord.ext import tasks, commands

client = commands.Bot(command_prefix='>>', self_bot=True)

@client.event
async def on_connect():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="my gf", details="In My Dream", state="She's so beautiful"))
	print("connected.")

client.run("fill me up baby", bot=False)
