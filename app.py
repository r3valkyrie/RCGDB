#!/usr/bin/env python3

"""
Reconcile Gaming Discord Bot

Assists with various tasks.
"""

import traceback
from discord.ext import commands
from modules.load_config import LoadConfig

description = """
RCGDB - Reconcile Gaming Discord Bot

Having issues? Report them here:
https://github.com/r3valkyrie/RCGDB/issues/new
"""

extensions = ['cogs.utils']

bot = commands.Bot(command_prefix='!', description=description)


@bot.command()
@commands.has_any_role(LoadConfig().role_whitelist)
async def load(ctx, extension_name: str):
    """
    Loads an extension.
    :param extension_name:
    :return:
    """

    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as ex:
        await ctx.send("```py\n{}: {}\n```".format(type(ex).__name__, str(ex)))

    await ctx.send("{} loaded".format(extension_name))


@bot.event
async def on_ready():
    print("Bot initialized!\n")
    async for guild in bot.fetch_guilds():
        print(f"Connected to {guild.name} as {bot.user}")

if __name__ == '__main__':
    print("Initializing bot...")
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)
            traceback.print_exc()

        try:
            bot.run(LoadConfig().token, bot=True, reconnect=True)
        except Exception as e:
            print(e)
            traceback.print_exc()
