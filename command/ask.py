import openai

def charmy_gpt(key,text):
    openai.api_key = key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text},
        ]
    )
    return response["choices"][0]["message"]["content"]