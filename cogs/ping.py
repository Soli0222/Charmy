import discord
from discord.ext import commands
from discord import app_commands
import settings

class PingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync(guild=discord.Object(int(settings.getId())))
        print("[Cogs] PingCog is ready.")

    @app_commands.command(name="ping", description="Botの応答を確認できます。")
    @app_commands.guilds(int(settings.getId()))
    async def hoge(self, interaction: discord.Interaction):
        await interaction.response.send_message("正常に稼働しています")

async def setup(bot: commands.Bot):
    await bot.add_cog(PingCog(bot))