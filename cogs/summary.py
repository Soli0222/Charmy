import discord
from discord.ext import commands
from discord import app_commands
import settings
import openai

def gpt(key,text):
    openai.api_key = key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "日本語で返して"},
            {"role": "system", "content": "与えられたリンク先を要約してください"},
            {"role": "user", "content": text},
        ]
    )
    return response["choices"][0]["message"]["content"]

class SummaryCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync(guild=discord.Object(int(settings.getId())))
        print("[Cogs] SummaryCog is ready.")

    @app_commands.command(
        name="summary",
        description="チャーミィがサイトを要約します WebサイトのURLを入力してください"
    )
    @app_commands.guilds(int(settings.getId()))
    async def summary(self, ctx:discord.Interaction, url: str):
        await ctx.response.defer()
        try:
            message = gpt(settings.getKey(),url)
        except Exception as e:
            message = "回答が見つからなかったか、内部でエラーが発生した可能性があります。"
            print(e)
        embed=discord.Embed(title=url, description=message, color=0xff9300)
        await ctx.followup.send(embed=embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(SummaryCog(bot))