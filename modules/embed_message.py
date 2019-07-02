from discord import Embed


class EmbedMsg:
    def __init__(self, desc):
        self._error_title = u"\u2757 Error!"
        self._error_color = 0xff3333
        self._success_title = u"\u2705 Success!"
        self._success_color = 0x7dd962

        self.error = Embed(
            title=self._error_title,
            description=str(desc),
            color=self._error_color
        )

        self.success = Embed(
            title=self._success_title,
            description=str(desc),
            color=self._success_color
        )

