# import instaloader
import logging
# import os
import requests
from bs4 import BeautifulSoup
import json

logging.basicConfig(level=logging.DEBUG)

# def get_recent_posts(username="kreativ.fr", max_posts=10):

def get_recent_posts(username="kreativ.fr"):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        ),
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    headers["Cookie"] = "ig_cb=1"
    
    resp = requests.get(url, headers=headers)
    print(resp.text[:1000])
    soup = BeautifulSoup(resp.text, "html.parser")
    
    scripts = soup.find("script", id="__NEXT_DATA__", type="application/json")
    if not scripts:
        logging.error("No scripts found in the page.")
        return []
    logging.debug(f"Found 1 script.")
    
    data = json.loads(scripts.string)
    try:
        edges = (
            data["props"]["pageProps"]["graphql"]["user"]
            ["edge_owner_to_timeline_media"]["edges"]
        )
    except KeyError:
        print("Structure inattendue, impossible de trouver les posts.")
        return []
 
    posts = []
    for edge in edges[:10]:
        node = edge["node"]
        posts.append({
            "shortcode": node["shortcode"],
            "url": f"https://www.instagram.com/p/{node['shortcode']}/",
            "image_url": node["display_url"],
            "caption": node["edge_media_to_caption"]["edges"][0]["node"]["text"]
                if node["edge_media_to_caption"]["edges"] else "",
            "date": node["taken_at_timestamp"],
        })
            
    return posts