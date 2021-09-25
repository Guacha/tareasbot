import os

import discord
from discord.ext import commands
from discord_slash import SlashCommand

token = os.environ.get('BOT_TOKEN')
test_guilds = [375866694465355776]
env = os.environ.get('ENV')

bot = commands.Bot(command_prefix=";")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Bot is ready! :D")
    
@slash.slash(
    name="ping",
    description="Ping the bot!",
    guild_ids=test_guilds
)
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(token)