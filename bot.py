from tareasbot import bot, token
from tareasbot.debug import Console

import os

console = Console("EXT")
console.separator()
console.log("Preparing to load modules")
for filename in os.listdir("./tareasbot/modules"):
    if filename.endswith(".py"):
        console.separator()
        console.debug_log(f"Loading module: {filename[:-3]}")
        bot.load_extension(f"tareasbot.modules.{filename[:-3]}")
console.log("Modules loaded successfully! :D")
console.separator()

console.debug_log("Running bot now")
bot.run(token)
