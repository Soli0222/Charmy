import discord
from dotenv import load_dotenv
import os
from os.path import join, dirname
from command.ask import charmy_gpt

if __name__=="__main__":
    load_dotenv(verbose=True)
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    DIS_TOKEN = os.environ.get("DISCORD_TOKEN")
    API_KEY = os.environ.get("OPENAI_API_KEY")
    SERVER_ID = os.environ.get("SERVER_ID")

    client = discord.Client(intents=discord.Intents.all())
    tree = discord.app_commands.CommandTree(client)

    @tree.command(
        name="ask",
        description="チャーミィになんでも質問できます。"
    )
    async def ask(ctx:discord.Interaction,text: str):
        await ctx.response.defer()

        try:
            message = charmy_gpt(API_KEY,text)
        except Exception as e:
            message = "回答が見つからなかったか、内部でエラーが発生した可能性があります。"
            print(e)
        
        embed=discord.Embed(title=text, description=message, color=0xff9300)
        await ctx.followup.send(embed=embed)

    @client.event
    async def on_ready():
        await tree.sync()
        #await tree.sync(guild=discord.Object(SERVER_ID))
        print('Startup! ServerID:',SERVER_ID)

    client.run(DIS_TOKEN)