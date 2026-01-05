import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

scope="user-library-read playlist-modify-public playlist-modify-private"

spotify_client_id = "56c49d501ecc4af5b39934f95f00f165"
spotify_client_secret = "6b82445c651649d5bcf6e3080898ca85"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret= spotify_client_secret,scope=scope, redirect_uri="https://example.com"))

text = input("Which year do you want to travel to? Type the date in this fomrat YYYY-MM-DD:")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(headers=header,url= URL+text)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_uris=[]
song_names = [song.getText().strip() for song in song_names_spans]
for song in song_names:
    response = sp.search(song)
    try:
        song_uris.append(response['tracks']['href'])
    except:
        print(f"{song} doesn't exist in Spotify. Skipped")

user_id = sp.current_user()["id"]

playlist=sp.user_playlist_create(user=user_id, name=f"{text}-playlist",public=False,collaborative=False,description="playlist of top 100 of the date")
print(song_uris)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id, song_uris,None)
#print(playlist["id"])