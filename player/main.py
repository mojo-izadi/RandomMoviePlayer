import json
import os
import random
import subprocess
import re

year_pattern = re.compile('\\d{4}')

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


def get_length(file):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
                             file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    duration = float(result.stdout)

    return duration / 60


def get_year(file):
    return int(year_pattern.search(file).group())


def get_movies_in_length_range(movies, min_length, max_length):
    to_return = []
    for movie in movies:
        length = get_length(movie)
        if (length >= min_length) & (length <= max_length):
            to_return += [movie, ]
    return to_return


def get_movies_in_year_range(movies, min_year, max_year):
    to_return = []
    for movie in movies:
        year = get_year(movie)
        if (year >= min_year) & (year <= max_year):
            to_return += [movie, ]
    return to_return

file = open('paths.json')
path_data = json.load(file)
movie_directory_path = path_data['movie_directory_path']
media_player_path = path_data['media_player_path']
file.close()

file = open('length.json')
path_data = json.load(file)
filter_by_length = path_data['filter_by_length']
min_length = float(path_data['min_length'])
max_length = float(path_data['max_length'])
file.close()

file = open('year.json')
path_data = json.load(file)
filter_by_year = path_data['filter_by_year']
min_year = path_data['min_year']
max_year = path_data['max_year']
file.close()

movies = getAllPlayableFiles(movie_directory_path)

if filter_by_year:
    movies = get_movies_in_year_range(movies, min_year, max_year)

if filter_by_length:
    movies = get_movies_in_length_range(movies, min_length, max_length)

movie = random.choice(movies)

subprocess.Popen([media_player_path, movie])
