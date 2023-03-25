import openai
import discord
import settings

def gpt(key,text):
    openai.api_key = key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "日本語で返して"},
            {"role": "user", "content": text},
        ]
    )
    return response["choices"][0]["message"]["content"]

def makeReply(text):
    try:
        message = gpt(settings.getKey(),text)
    except Exception as e:
        message = "回答が見つからなかったか、内部でエラーが発生した可能性があります。"
        print(e)
    
    embed=discord.Embed(title=text, description=message, color=0xff9300)
    return embed