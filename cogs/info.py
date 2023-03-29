import discord
from discord.ext import commands
from discord import app_commands
import settings
import datetime

class InfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync(guild=discord.Object(int(settings.getId())))
        print("[Cogs] InfoCog is ready.")

    @app_commands.command(name="info", description="Botの情報を確認できます")
    @app_commands.guilds(int(settings.getId()))
    async def hoge(self, interaction: discord.Interaction):
        dt_now = datetime.datetime.now()
        await interaction.response.send_message("Charmy for Xanadu by Soli\nVersion: Rev 0.0.4\nUpdated: 2023/03/29\n"+dt_now.strftime('%Y/%m/%d/ %H:%M:%S'))

async def setup(bot: commands.Bot):
    await bot.add_cog(InfoCog(bot))