import GUI
import json
import os
import random
import re
import cv2

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
    video = cv2.VideoCapture(file)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    return frame_count / (fps * 60)


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
file.close()

movies = getAllPlayableFiles(movie_directory_path)

filter_by_year, min_year, max_year, filter_by_length, min_length, max_length = GUI.create_GUI()

if filter_by_year:
    movies = get_movies_in_year_range(movies,
                                      int(min_year) if min_year != '' else -1,
                                      int(max_year) if max_year != '' else 10000)

if filter_by_length:
    movies = get_movies_in_length_range(movies,
                                        float(min_length) if min_length != '' else -1,
                                        float(max_length) if max_length != '' else 10000)

if len(movies) == 0:
    GUI.show_error_message_box()
else:
    movie = random.choice(movies)
    os.startfile(movie)
