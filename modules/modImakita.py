import openai
import discord
import settings

def gpt(key,texts):
    openai.api_key = key

    messages=[
            {"role": "system", "content": "会話文を3行に要約する人です"},
            {"role": "system", "content": "与えられる会話文は「[名前]#[ID]:[メッセージ]」の形式です"},
    ]

    for text in texts:
        messages.append({"role": "user", "content": text})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response["choices"][0]["message"]["content"]

def makeReply(texts,hour):
    try:
        message = gpt(settings.getKey(),texts)
    except Exception as e:
        message = "回答が見つからなかったか、内部でエラーが発生した可能性があります。"
        print(e)
    
    embed=discord.Embed(title=str(hour)+"時間分の会話を要約しました", description=message, color=0x00ffff)
    return embed