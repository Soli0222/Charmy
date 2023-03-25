import settings
import discord
from discord.ext import commands

INITAL_EXTENSIONS = [
    "cogs.ask",
    "cogs.ask_eph",
    "cogs.info",
    "cogs.summary"

]

class Charmy(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
        )
    
    async def setup_hook(self):
        for extension in INITAL_EXTENSIONS:
            await self.load_extension(extension)

if __name__ == '__main__':
    bot_token = settings.getToken()
    Charmy().run(bot_token)
