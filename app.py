#!/usr/bin/env python3

"""
Reconcile Gaming Discord Bot

Assists with various tasks.
"""

import traceback
import json
from discord.ext import commands

with open('config.json', 'r') as config:
    c_data = json.loads(config)
    token = c_data['token']
    role_whitelist = " ".join(c_data['role_whitelist'])

description = """
RCGDB - Reconcile Gaming Discord Bot

Having issues? Report them here:
https://github.com/r3valkyrie/RCGDB/issues/new
"""

extensions = ['cogs.utils']

bot = commands.Bot(command_prefix='!', description=description)


@bot.command()
@commands.has_any_role(role_whitelist)
async def load(ctx, extension_name: str):
    """
    Loads an extension.
    :param extension_name:
    :return:
    """

    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))

    await ctx.send("{} loaded".format(extension_name))

if __name__ == '__main__':
    print(role_whitelist)
    print(token)
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)
            traceback.print_exc()

        try:
            bot.run(token, bot=True, reconnect=True)
        except Exception as e:
            print(e)
            traceback.print_exc()