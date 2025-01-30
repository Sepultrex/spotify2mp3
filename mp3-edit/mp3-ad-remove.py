import os

def rename_mp3_files(directory):
    new_filenames = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".mp3"):
                # Removes [music-download-blabla.com] from filename
                new_filename = filename.replace("[music-download-blabla.com]", "")
                new_filenames.append(new_filename)
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

        with open(os.path.join(directory, "log.txt"), "w", encoding="utf-8") as file:
            for name in new_filenames:
                file.write(name + "\n")
        print("Successfully changed file names and saved in log.txt")
    except FileNotFoundError:
        print(f"mp3 files not found: {directory}")
    except Exception as e:
        print(f"err: {e}")

# location of mp3 files
rename_mp3_files(r"sinop\music")
