import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

from cogs import stream

bot = commands.Bot(command_prefix="cock:", intents=discord.Intents.all(),)

cogs = [stream]

for cog in cogs:
    asyncio.get_event_loop().run_until_complete(cog.setup(bot))

bot.run(os.getenv("TOKEN"))
