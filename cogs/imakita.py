import discord
from discord.ext import commands
from discord import app_commands
import settings
import datetime
from modules.modImakita import makeReply

class ImakitaCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync(guild=discord.Object(int(settings.getId())))
        print("[Cogs] ImakitaCog is ready.")

    @app_commands.command(name="imakita", description="指定した時間分の会話を要約します")
    @app_commands.guilds(int(settings.getId()))

    async def imakita(self, interaction: discord.Interaction, hour: int):
        await interaction.response.defer()

        end_time = datetime.datetime.now()
        start_time = end_time - datetime.timedelta(hours=hour)

        text = []
        async for message in interaction.channel.history(limit=None, after=start_time, before=end_time):
            text.append(f"{message.author}: {message.content}")

        await interaction.followup.send(embed=makeReply(text,hour))
        

async def setup(bot: commands.Bot):
    await bot.add_cog(ImakitaCog(bot))