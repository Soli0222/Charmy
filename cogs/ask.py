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
            {"role": "user", "content": text},
        ]
    )
    return response["choices"][0]["message"]["content"]

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
        description="チャーミィになんでも質問できます。"
    )
    @app_commands.guilds(int(settings.getId()))
    async def ask(self, ctx:discord.Interaction, text: str):
        await ctx.response.defer()
        try:
            message = gpt(settings.getKey(),text)
        except Exception as e:
            message = "回答が見つからなかったか、内部でエラーが発生した可能性があります。"
            print(e)
        embed=discord.Embed(title=text, description=message, color=0xff9300)
        await ctx.followup.send(embed=embed)
        
async def setup(bot: commands.Bot): # この関数が超重要
    await bot.add_cog(AskCog(bot))