import os
from mutagen.easyid3 import EasyID3

def update_mp3_filenames(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            
            try:
                audio = EasyID3(file_path)
                
                contributor = audio.get('artist', ['Unknown Artist'])[0]
                
                new_filename = f"{contributor} - {filename}"
                new_file_path = os.path.join(folder_path, new_filename)
                
                os.rename(file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            
            except Exception as e:
                print(f"err '{filename}': {e}")

# location of mp3 files
folder_path = r'C:\Users\sinop\Desktop\ae'
update_mp3_filenames(folder_path)
