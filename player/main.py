import json
import os
import random
import subprocess

def getAllPlayableFiles(path):
    to_return = []
    all_files = [os.path.join(path, x) for x in os.listdir(path)]
    to_return += [x for x in all_files if isPlayableFile(x)]
    all_folders = [x for x in all_files if not (os.path.isfile(x))]

    for folder in all_folders:
        to_return += getAllPlayableFiles(folder)

    return to_return

def isPlayableFile(file_path):
    return file_path.endswith(".mkv") | file_path.endswith(".mp4") | file_path.endswith(".webm")

file = open('paths.json')
path_data = json.load(file)
movie_directory_path = path_data['movie_directory_path']
media_player_path = path_data['media_player_path']
file.close()

movies = getAllPlayableFiles(movie_directory_path)

movie = random.choice(movies)

subprocess.Popen([media_player_path, movie])

