import discord
from discord.ext import commands
from discord import app_commands
import settings
from modules.modAsk import makeReply

class AskEphCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync(guild=discord.Object(int(settings.getId())))
        print("[Cogs] AskEphCog is ready.")

    @app_commands.command(
        name="ask_eph",
        description="チャーミィになんでも質問できます 回答は自分以外の誰にも見られない形になります"
    )
    @app_commands.guilds(int(settings.getId()))
    async def ask(self, ctx:discord.Interaction, text: str):
        await ctx.response.defer(ephemeral=True)
        
        embed = makeReply(text)

        await ctx.followup.send(embed=embed,ephemeral=True)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(AskEphCog(bot))