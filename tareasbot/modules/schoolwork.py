import discord
from discord.ext.commands import command, Cog

from .. import DB, test_guilds
from ..debug import Console

from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option


class Homework(Cog):

    def __init__(self, bot):
        Console.debug_log("Initialising module", module="HOMEWORK")
        self.bot = bot

    @cog_ext.cog_subcommand(
        base="cursos",
        name="mostrar",
        guild_ids=test_guilds,
        description="Mostrar todos los cursos disponibles"
    )
    async def show_all_courses(self, ctx: SlashContext):
        Console.debug_log(f"Command: cursos mostrar, User: {ctx.author.name} ({ctx.author_id})", module="HOMEWORK")
        cursos = DB.get_courses()
        embed = discord.Embed(title="Me quiero morir", description="Estos son los cursos registrados en mi Base de "
                                                                   "datos")
        for curso in cursos:
            embed.add_field(name=f"{curso.course_dept} {curso.course_code}", value=f"{curso.name}", inline=True)

        await ctx.send("Holis", embed=embed)

    @cog_ext.cog_subcommand(
        base="cursos",
        name="agregar",
        guild_ids=test_guilds,
        description="Agregar curso nuevo",
        options=[
            create_option(
                name="departamento",
                description="Departamento para el curso a agregar, usualmente algo como IST o MAT",
                option_type=3,
                required=True
            ),
            create_option(
                name="codigo",
                description="Código para el curso a agregar (4 dígitos), usualmente algo como 2088 o 4032",
                option_type=4,
                required=True
            ),
            create_option(
                name="nombre",
                description="Nombre del curso a agregar, algo como Algoritmia I o Cálculo III",
                option_type=3,
                required=True
            ),

        ]
    )
    async def add_course(self, ctx: SlashContext, departamento, codigo, nombre):
        await ctx.send(f"Course: {departamento}{codigo}: {nombre}")


def setup(bot):
    bot.add_cog(Homework(bot))
