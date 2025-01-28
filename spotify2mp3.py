import os
import time
import yt_dlp
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# spotify api
SPOTIPY_CLIENT_ID = 'clientid'
SPOTIPY_CLIENT_SECRET = 'clientsecret'

# ffmpeg konumu
FFMPEG_LOCATION = r'ffmpegkonumu'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

def download_song(track_name, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'ffmpeg_location': FFMPEG_LOCATION,
        'noplaylist': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{track_name}"])

def get_spotify_playlist_tracks(playlist_url):
    playlist_id = playlist_url.split('/')[-1].split('?')[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = [item['track'] for item in results['items']]
    return tracks

def get_spotify_track_info(track_url):
    track_id = track_url.split('/')[-1].split('?')[0]
    track = sp.track(track_id)
    return track

def main():
    print("1. Çalma listesi indir")
    print("2. Tek şarkı indir")
    choice = input("Seçiminizi yapın (1/2): ")

    output_path = input("İndirilecek dosya yolunu girin: ")

    if choice == "1":
        playlist_url = input("Spotify çalma listesi URL'sini girin: ")
        tracks = get_spotify_playlist_tracks(playlist_url)
        
        for index, track in enumerate(tracks):
            track_name = f"{track['name']} - {track['artists'][0]['name']}"
            print(f"İndiriliyor: {track_name}")
            download_song(track_name, output_path)
            
            if (index + 1) % 5 == 0:
                print("5 şarkı indirildi, 5 saniye bekleniyor...")
                time.sleep(5)
    elif choice == "2":
        track_url = input("Spotify şarkı URL'sini girin: ")
        track = get_spotify_track_info(track_url)
        track_name = f"{track['name']} - {track['artists'][0]['name']}"
        print(f"İndiriliyor: {track_name}")
        download_song(track_name, output_path)
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
