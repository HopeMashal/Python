import requests
import time
from dotenv import load_dotenv

load_dotenv()
import os

#global variables
api_key = os.getenv("api_key")
bot_key = os.getenv("bot_key")
chat_id = os.getenv("chat_id")

limit = 59000
time_interval = 5 * 60

def get_price():
  url=""