from dotenv import load_dotenv
import os
from os.path import join, dirname

def load_env():
    load_dotenv(verbose=True)
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    DIS_TOKEN = os.environ.get("DISCORD_TOKEN")
    SERVER_ID = os.environ.get("SERVER_ID")
    API_KEY = os.environ.get("OPENAI_API_KEY")

    return DIS_TOKEN, SERVER_ID, API_KEY

if __name__=="__main__":
    print(load_env())