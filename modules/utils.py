import json
from discord.ext import commands
from discord import Embed

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

                # Confirmation dialogue
                _share_msg_success = Embed(
                    title=u"\u2705 Success!",
                    description=f"""
                    {ctx.author.mention}
                    Click the link below to begin screen sharing in your voice channel!\n
                    https://www.discordapp.com/channels/{ctx.guild.id}/{ctx.author.voice.channel.id}
                    """,
                    color=0x7dd962
                )
                await ctx.send(embed=_share_msg_success)
        except Exception as e:

            # Error dialogue

            _no_voice_error = Embed(
                title=u"\u2757 Error!",
                description="You are not currently in a "
                "voice channel. Please join a voice channel, then "
                "re-try this command.",
                color=0xff3333
            )
            await ctx.send(embed=_no_voice_error)
            raise e


def setup(bot):
    bot.add_cog(Utils(bot))
