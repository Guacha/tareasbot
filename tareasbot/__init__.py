import os

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

from .database import Database
from .debug import Console

console = Console("MAIN")

console.separator()
console.log("Initialising bot")
console.log("Connecting to Database")
DB = Database()
console.separator()

console.log(
    "Getting environment variables for the bot. The variables must be defined for the bot to successfully connect to "
    "the Discord Client API")
token = os.environ.get('BOT_TOKEN')
test_guilds = [375866694465355776, 699275030412132373]
admin_users = [301155670793781248, 681593196119195730]
env = os.environ.get('ENV')
console.log("Variables loaded successfully!")

bot = commands.Bot(command_prefix=";")
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    console.debug_log("Event: on_ready")
    console.log("Bot is up and ready :D")


@slash.slash(
    name="ping",
    description="Ping the bot!",
    guild_ids=test_guilds
)
async def ping(ctx: SlashContext):
    console.debug_log(f"Command: ping, User: {ctx.author.name} ({ctx.author_id})")
    await ctx.send(f"Pong! (Response time: {bot.latency * 1000})")

