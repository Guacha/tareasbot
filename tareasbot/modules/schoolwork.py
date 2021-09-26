import discord
from discord.ext.commands import command, Cog

from discord_slash import cog_ext
from discord_slash.utils.manage_commands import SlashContext, create_choice, create_option

from .. import DB, test_guilds

class Homework(Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @cog_ext.cog_slash(
        name="cursos",
        description="Obtener todos los cursos registrados",
        guild_ids=test_guilds
    )
    async def get_courses(self, ctx: SlashContext):
        c = DB.get_courses()
        print(c)
        await ctx.send("Mira la consola pa")
        
        
def setup(bot):
    bot.add_cog(Homework(bot))