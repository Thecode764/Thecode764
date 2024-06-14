

import requests
import json
def get_stock_data():
    url = "https://api.github.com/users/Thecode764"
    response = requests.get(url)
     
    if response.status_code == 200:
        data = response.json()
        followers = data['followers']
        following = data['following']
        public_repos = data['public_repos']
        file = open("stats.svg", "w+")
        file.write(f"""
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="10" width="180" height="180" rx="10" ry="10" fill="black" />

    <text x="19" y="28" font-size="15px" font-family="monospace" fill="white">Thecode764</text>
    <text x="19" y="50" font-size="10px" font-family="monospace" fill="white">Followers:                                {followers}</text>
    <text x="19" y="78" font-size="10px" font-family="monospace" fill="white">Following:     {following}</text>
    <text x="19" y="109" font-size="10px" font-family="monospace" fill="white">Public repositories:     {public_repos}</text>
</svg>

""")
    else:
        print("Rate limited")