import discord
from discord.ext.commands import command, Cog

from .. import DB, test_guilds
from ..debug import Console

from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option


class CourseCog(Cog):

    def __init__(self, bot):
        self.console = Console("COURSES")
        self.console.debug_log("Initialising module")
        self.bot = bot

    @cog_ext.cog_subcommand(
        base="cursos",
        name="mostrar",
        guild_ids=test_guilds,
        description="Mostrar todos los cursos disponibles"
    )
    async def show_all_courses(self, ctx: SlashContext):
        """
        Command that shows all available courses in an embed, should also allow in the future to scroll through all
        courses
        TODO: Implement a way to scroll through courses
        Args:
            ctx: The Slash context the function is called with. Given by the Discord API
        """

        self.console.debug_log(f"Command: cursos mostrar, User: {ctx.author.name} ({ctx.author_id})")
        cursos = DB.get_courses()
        embed = discord.Embed(title="Me quiero morir", description="Estos son los cursos registrados en mi Base de "
                                                                   "datos")
        for curso in cursos:
            embed.add_field(name=f"{curso.course_dept} {curso.course_code}", value=f"{curso.name}", inline=True)

        await ctx.send("Aquí tengo la información que solicitaste", embed=embed)

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
    async def add_course(self, ctx: SlashContext, departamento: str, codigo: int, nombre: str) -> None:
        departamento = departamento.upper()
        codigo = str(codigo)
        nombre.capitalize()
        self.console.debug_log(f"Command: cursos agregar {departamento} {codigo}, {nombre}, User: "
                               f"{ctx.author.name} ({ctx.author_id})")
        if len(departamento) != 3:
            self.console.err("Command failed: Dept name error")
            await ctx.send("El nombre del departamento no es válido, debe ser una cadena de 3 caracteres")
            return

        if len(codigo) < 3:
            self.console.err("Command failed: Course code error")
            await ctx.send("El código de la asignatura no es válida, debe ser un entero de al menos 4 y no mas de 6 "
                           "caracteres")
            return
        self.console.debug_log("Calling DB Function: add_course()")
        DB.add_course(departamento, codigo, nombre)
        await ctx.send("He agregado el curso satisfactoriamente uwu")


def setup(bot):
    bot.add_cog(CourseCog(bot))
