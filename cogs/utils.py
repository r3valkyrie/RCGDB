import json
from modules.embed_message import EmbedMsg
from discord.ext import commands
from inspect import cleandoc

with open('config.json') as config:
    c_data = json.load(config)
    token = c_data['token']
    role_whitelist = c_data['role_whitelist']


class Utils(commands.Cog, name="Utils"):
    """
    Various utilities.
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def share(self, ctx):
        """
        Generates a link to share your screen in the current voice channel.
        :param ctx:
        :return:
        """

        try:
            if ctx.author.voice.channel is not None:

                description = cleandoc(f"""
                Click the link below to begin screen sharing in voice channel: \U0001F56A {ctx.author.voice.channel.name}\n
                https://www.discordapp.com/channels/{ctx.guild.id}/{ctx.author.voice.channel.id}
                """)

                await ctx.send(embed=EmbedMsg(description).success)
        except Exception as e:

            description = cleandoc("""You are not currently in a \
            voice channel. Please join a voice channel and \
            run this command again.""")

            await ctx.send(embed=EmbedMsg(description).error)
            raise e


def setup(bot):
    bot.add_cog(Utils(bot))
