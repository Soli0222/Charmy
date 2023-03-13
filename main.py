import discord
from command.ask import charmy_gpt
import settings

if __name__=="__main__":
    bot_token, server_id, api_key = settings.load_env()
    client = discord.Client(intents=discord.Intents.all())
    tree = discord.app_commands.CommandTree(client)

    @tree.command(
        name="ask",
        description="チャーミィになんでも質問できます。"
    )
    async def ask(ctx:discord.Interaction,text: str):
        await ctx.response.defer()

        try:
            message = charmy_gpt(api_key,text)
        except Exception as e:
            message = "回答が見つからなかったか、内部でエラーが発生した可能性があります。"
            print(e)
        
        embed=discord.Embed(title=text, description=message, color=0xff9300)
        await ctx.followup.send(embed=embed)

    @client.event
    async def on_ready():
        #await tree.sync()
        await tree.sync(guild=discord.Object(server_id))
        print('Startup! ServerID:',server_id)

    client.run(bot_token)