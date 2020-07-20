import requests
from aybapi.Bot import Bot
from aybapi.Category import Category

base = "https://api.ayblisting.com"

class Client:
  def fetch_stats(self):
    res = requests.get(f'{base}/stats')
    return res.json()
  
  def fetch_bot(self, id):
    res = requests.get(f'{base}/bot?id={id}')
    return Bot(self, res.json())

  def fetch_category(self, id):
    res = requests.get(f'{base}/category?id={id}')
    return Category(res.json())
