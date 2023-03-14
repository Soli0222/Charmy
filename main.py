import settings
import discord
from discord.ext import commands

bot_token = settings.getToken()
server_id = settings.getId()
api_key = settings.getKey()

INITAL_EXTENSIONS = [
    "cogs.ask",
    "cogs.ping"

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
    Charmy().run(bot_token)
