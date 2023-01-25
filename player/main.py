import json
import os
import random
import subprocess

file = open('paths.json')
path_data = json.load(file)
movie_directory_path = path_data['movie_directory_path']
media_player_path = path_data['media_player_path']
file.close()


movie = random.choice(os.listdir(movie_directory_path))
movie_path = os.path.join(movie_directory_path, movie)
movie_file_name = [x for x in os.listdir(movie_path) if x.endswith(".mkv") | x.endswith(".mp4")][0]
movie_file_path = os.path.join(movie_path, movie_file_name)

p = subprocess.Popen([media_player_path, movie_file_path])

