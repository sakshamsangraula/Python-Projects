from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

# ask the user for a date and scrape the top 100 song titles in Billboard Top 100 from that date
date = input("What year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
URL_with_date = f"{BILLBOARD_URL}{date}"
# class="chart-element__information__song text--truncate color--primary"
response = requests.get(URL_with_date)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_spans_with_class = soup.find_all(name="span",
                            class_="chart-element__information__song text--truncate color--primary")
song_titles = [span.getText() for span in all_spans_with_class]
# print(song_titles)


# successfully authenticated to spotify using the client id and client secret env variables
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
spotify_oauth = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                            client_id="CLIENT ID",
                                            client_secret="CLIENT SECRET",
                                            scope="playlist-modify-private",
                                            redirect_uri="REDIRECT URI",
                                            show_dialog=True,
                                            cache_path="token.txt"
                                            ))

user_id = spotify_oauth.current_user()["id"]
year = date.split("-")[0]
song_uris = []
for song in song_titles:
    result = spotify_oauth.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# create a playlist
playlist_name = f"{date} Billboard Top 100"
playlist = spotify_oauth.user_playlist_create(user=user_id, name=playlist_name, public=False)

# add songs to playlist
spotify_oauth.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
# user_info = spotify_oauth.current_user()
# print(user_info)
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])