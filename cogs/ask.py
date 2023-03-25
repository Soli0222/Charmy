import discord
from discord.ext import commands
from discord import app_commands
import settings
from modules.modAsk import makeReply

class AskCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync(guild=discord.Object(int(settings.getId())))
        print("[Cogs] AskCog is ready.")

    @app_commands.command(
        name="ask",
        description="チャーミィになんでも質問できます"
    )
    @app_commands.guilds(int(settings.getId()))
    async def ask(self, ctx:discord.Interaction, text: str):
        await ctx.response.defer()
        
        embed = makeReply(text)

        await ctx.followup.send(embed=embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(AskCog(bot))