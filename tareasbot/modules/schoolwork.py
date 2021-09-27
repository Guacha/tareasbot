import discord
from discord.ext.commands import command, Cog

from .. import DB, test_guilds
from ..debug import Console

from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option


class HomeworkCog(Cog):

    def __init__(self, bot):
        self.console = Console("HOMEWORK")
        self.console.debug_log("Initialising module")
        self.bot = bot


def setup(bot):
    bot.add_cog(HomeworkCog(bot))
