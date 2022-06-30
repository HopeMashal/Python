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
  url="https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
  }

  response = requests.get(url, headers=headers).json()
  btc_price = response['data'][0]['quote']['USD']['price']
  return btc_price

