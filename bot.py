from tareasbot import bot, token
from tareasbot.debug import Console

import os

Console.separator()
Console.log("Preparing to load modules", module="EXT")
for filename in os.listdir("./tareasbot/modules"):
    if filename.endswith(".py"):
        Console.separator()
        Console.debug_log(f"Loading module: {filename[:-3]}", module="EXT")
        bot.load_extension(f"tareasbot.modules.{filename[:-3]}")

bot.run(token)
