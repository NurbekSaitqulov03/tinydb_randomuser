import requests

base_url = "https://randomuser.me/api/"
payload = {
    'results':5
}

r = requests.get(url=base_url, params=payload)
