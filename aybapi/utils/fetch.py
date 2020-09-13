import requests


def fetch(url):
    res = requests.get(url)
    return res.json()
